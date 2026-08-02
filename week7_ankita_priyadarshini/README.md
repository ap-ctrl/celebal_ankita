# 📄 Document Question Answering System (RAG)

A beginner-friendly Retrieval-Augmented Generation (RAG) system that answers questions from custom PDF documents using semantic search and a Large Language Model (LLM).

---

## 🚀 Overview

This project allows users to upload a PDF document and ask natural language questions about its contents.

Instead of relying solely on an LLM's internal knowledge, the application retrieves the most relevant sections of the uploaded document and provides them as context to the LLM, ensuring more accurate and document-grounded responses.

---

## ✨ Features

- Upload custom PDF documents
- Extract text from PDFs
- Split text into semantic chunks
- Generate embeddings using Sentence Transformers
- Store embeddings using FAISS
- Retrieve the most relevant chunks
- Generate answers using Groq's Llama model
- Interactive Streamlit web interface
- Display retrieved context used for answer generation

---

## 🏗️ System Architecture

```
                PDF Upload
                     │
                     ▼
           Document Ingestion
                     │
                     ▼
              Text Chunking
                     │
                     ▼
         Sentence Embeddings
                     │
                     ▼
             FAISS Vector Store
                     │
──────────────────────────────────────
                     │
             User Question
                     │
                     ▼
         Question Embedding
                     │
                     ▼
         Similarity Search (FAISS)
                     │
                     ▼
      Retrieve Relevant Chunks
                     │
                     ▼
     Groq Llama Language Model
                     │
                     ▼
              Generated Answer
```

---

## 🛠️ Technologies Used

| Technology               | Purpose              |
| ------------------------ | -------------------- |
| Python                   | Programming Language |
| Streamlit                | Web Interface        |
| PyMuPDF                  | PDF Text Extraction  |
| Sentence Transformers    | Embedding Generation |
| FAISS                    | Vector Database      |
| Groq API                 | LLM Inference        |
| LangChain Text Splitters | Text Chunking        |

---

## 📂 Project Structure

```
RAG_Project/

│
├── app.py
├── config.py
├── requirements.txt
├── README.md
│
├── data/
│
├── modules/
│   ├── loader.py
│   ├── chunker.py
│   ├── embedding.py
│   ├── vector_store.py
│   ├── retriever.py
│   └── generator.py
│
├── vector_db/
│
└── .env
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project

```bash
cd <repository-name>
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file.

```
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 📖 Workflow

1. Upload a PDF document
2. Extract text from the PDF
3. Split text into chunks
4. Generate embeddings
5. Store embeddings in FAISS
6. Ask a question
7. Retrieve relevant chunks
8. Generate an answer using Groq Llama

---

## 📌 Future Improvements

- Support multiple PDF uploads
- Add document caching
- Hybrid search (Keyword + Vector)
- Re-ranking of retrieved documents
- Chat history
- Multiple embedding models
- Support DOCX and TXT files

---

## 📜 License

This project is created for learning and educational purposes.
