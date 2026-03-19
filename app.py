import streamlit as st
import time
from rag_pipeline import process_pdf, answer_question_stream

st.set_page_config(page_title="AI PDF Chatbot", layout="wide")

st.title("💬 AI PDF Chatbot")

# ----------------------------
# FILE UPLOAD
# ----------------------------
uploaded_file = st.file_uploader("Upload PDF", type="pdf")

if uploaded_file:
    if st.button("Process PDF"):
        progress = st.progress(0)

        def update(p):
            progress.progress(p)

        with st.spinner("Processing PDF..."):
            process_pdf(uploaded_file, update)

        st.success("✅ PDF ready")

# ----------------------------
# INPUT
# ----------------------------
question = st.text_input("Ask a question")

if question:

    start_time = time.time()

    # Thinking indicator
    thinking = st.empty()
    thinking.write("🤔 Thinking...")

    stream = answer_question_stream(question)

    response_box = st.empty()
    full_answer = ""

    # Streaming output
    for chunk in stream:
        full_answer += chunk
        response_box.markdown(full_answer + "▌")
        time.sleep(0.01)

    thinking.empty()

    response_box.markdown(full_answer)

    end_time = time.time()

    st.write(f"⏱ Response time: {round(end_time - start_time, 2)} sec")