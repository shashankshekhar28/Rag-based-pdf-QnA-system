import faiss
import numpy as np
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer, CrossEncoder
import ollama

# Lazy load models
embedding_model = None
reranker = None

chunks = []
index = None


def load_models():
    global embedding_model, reranker

    if embedding_model is None:
        embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

    if reranker is None:
        reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")


# ----------------------------
def chunk_text(text, chunk_size=200, overlap=50):
    words = text.split()
    chunks = []
    start = 0

    while start < len(words):
        chunk = " ".join(words[start:start + chunk_size])
        chunks.append(chunk)
        start += chunk_size - overlap

    return list(set(chunks))


# ----------------------------
def process_pdf(uploaded_file, progress_callback=None):
    global chunks, index

    load_models()

    reader = PdfReader(uploaded_file)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text

    if progress_callback:
        progress_callback(40)

    chunks = chunk_text(text)[:200]

    if progress_callback:
        progress_callback(70)

    embeddings = embedding_model.encode(chunks,
    batch_size=32,
    show_progress_bar=False,
    convert_to_numpy=True)

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))

    if progress_callback:
        progress_callback(100)


# ----------------------------
def retrieve(query):
    query_embedding = embedding_model.encode([query])
    _, indices = index.search(np.array(query_embedding),3)
    return [chunks[i] for i in indices[0]]


# ----------------------------
def rerank(query, passages):
    pairs = [[query, p] for p in passages]
    scores = reranker.predict(pairs)

    ranked = sorted(zip(passages, scores),
                    key=lambda x: x[1],
                    reverse=True)

    return [r[0] for r in ranked[:2]]


# ----------------------------
def stream_answer(prompt):
    stream = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}],
        stream=True
    )

    for chunk in stream:
        yield chunk["message"]["content"]


# ----------------------------
def answer_question_stream(question):

    retrieved = retrieve(question)
    best_chunks = retrieved[:2]   # skip reranker

    context = "\n".join(best_chunks)

    prompt = f"""
Answer using ONLY this context.

Context:
{context}

Question: {question}

Answer in one short sentence.
"""

    return stream_answer(prompt)