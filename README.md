# 📄 PDF QnA System (RAG + LLaMA)

## 🚀 Overview

This project is a **Retrieval-Augmented Generation (RAG)** based AI chatbot that allows users to upload PDF documents and ask questions in natural language.

Instead of relying on general knowledge, the system retrieves relevant information from the uploaded document and generates **accurate, context-aware answers** using a local LLM.

---

## ✨ Features

* 📂 Upload any PDF document
* 💬 Ask questions in natural language
* ⚡ Real-time streaming responses (ChatGPT-like typing effect)
* 🤔 Thinking indicator before response generation
* 🧠 Context-aware answers using semantic search
* 🤖 Local LLaMA model (no API required)
* ⏱ Fast response time with optimized pipeline

---

## 🧠 How It Works

```
PDF → Chunking → Embeddings → FAISS → Retrieval → LLaMA → Answer
```

* **Chunking**: Splits document into smaller parts
* **Embeddings**: Converts text into vector representations
* **FAISS**: Performs fast similarity search
* **Retrieval**: Selects relevant context
* **LLaMA**: Generates final answer

---

## 🛠 Tech Stack

* Python
* Streamlit
* Sentence Transformers
* FAISS (Vector Database)
* Ollama (LLaMA 3 - Local LLM)

---

## ⚡ Performance Optimizations

* 🚀 Reduced latency by ~60% using:

  * Lightweight embeddings (**all-MiniLM-L6-v2**)
  * Reduced retrieval size
  * Removed reranking overhead for faster inference

* ⚡ Improved UI responsiveness with:

  * Token streaming
  * Buffered rendering
  * Reduced unnecessary delays

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/shashankshekhar28/Rag-based-pdf-QnA-system.git
cd Rag-based-pdf-QnA-system
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Install and run LLaMA locally

Download Ollama: https://ollama.com

```bash
ollama run llama3
```

### 4. Run the Streamlit app

```bash
streamlit run app.py
```

---

## 💡 Use Cases

* 📚 Students querying textbooks
* 📄 Resume analysis and extraction
* 📑 Research paper exploration
* 🏢 Enterprise document search systems

---

## 🚀 Future Improvements

* 📄 Highlight answers inside PDF
* 📚 Multi-document support
* 🌐 Cloud deployment
* 🎤 Voice-based interaction

---

## 👨‍💻 Author

**Shashank Shekhar**
GitHub: https://github.com/shashankshekhar28

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!
