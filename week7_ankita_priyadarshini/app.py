import streamlit as st
import os

from modules.loader import load_pdf
from modules.chunker import split_text
from modules.embedding import create_embeddings
from modules.vector_store import save_vectors
from modules.retriever import load_vector_database, retrieve_chunks
from modules.generator import generate_answer

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Document Question Answering System",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Document Question Answering System (RAG)")
st.write("Upload a PDF and ask questions about it.")

# -------------------------------
# Session State Initialization
# -------------------------------
if "index" not in st.session_state:
    st.session_state.index = None

if "chunks" not in st.session_state:
    st.session_state.chunks = None

if "current_file" not in st.session_state:
    st.session_state.current_file = None

# -------------------------------
# Upload PDF
# -------------------------------
uploaded_file = st.file_uploader(
    "Upload your PDF",
    type=["pdf"]
)

# -------------------------------
# Process PDF only if it's a new file
# -------------------------------
if uploaded_file is not None:

    if uploaded_file.name != st.session_state.current_file:

        # Save uploaded PDF
        pdf_path = os.path.join("data", "uploaded.pdf")

        with open(pdf_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        with st.spinner("Reading PDF..."):
            text = load_pdf(pdf_path)

        with st.spinner("Splitting into chunks..."):
            chunks = split_text(text)

        with st.spinner("Generating embeddings..."):
            embeddings = create_embeddings(chunks)

        with st.spinner("Creating vector database..."):
            save_vectors(embeddings, chunks)

        # Load vector database
        index, stored_chunks = load_vector_database()

        # Save in Session State
        st.session_state.index = index
        st.session_state.chunks = stored_chunks
        st.session_state.current_file = uploaded_file.name

        st.success("✅ PDF processed successfully!")

# -------------------------------
# Ask Questions
# -------------------------------
if st.session_state.index is not None:

    question = st.text_input(
        "Ask a question about your document:"
    )

    if st.button("Get Answer"):

        if question.strip() == "":
            st.warning("Please enter a question.")

        else:

            with st.spinner("Retrieving relevant information..."):

                retrieved_chunks = retrieve_chunks(
                    question,
                    st.session_state.index,
                    st.session_state.chunks
                )

                context = "\n\n".join(retrieved_chunks)

            with st.spinner("Generating answer..."):

                answer = generate_answer(
                    question,
                    context
                )

            st.subheader("Answer")

            st.write(answer)

            with st.expander("Retrieved Context"):

                for i, chunk in enumerate(retrieved_chunks):

                    st.markdown(f"### Chunk {i+1}")

                    st.write(chunk)

# import streamlit as st

# from modules.loader import load_pdf
# from modules.chunker import split_text
# from modules.embedding import create_embeddings
# from modules.vector_store import save_vectors
# from modules.retriever import (
#     load_vector_database,
#     retrieve_chunks
# )
# from modules.generator import generate_answer

# st.set_page_config(page_title="Simple RAG")

# st.title("📄 Document Question Answering System")

# uploaded_file = st.file_uploader(
#     "Upload PDF",
#     type=["pdf"]
# )

# if uploaded_file is not None:

#     with open("data/uploaded.pdf", "wb") as f:
#         f.write(uploaded_file.read())

#     text = load_pdf("data/uploaded.pdf")

#     chunks = split_text(text)

#     embeddings = create_embeddings(chunks)

#     save_vectors(embeddings, chunks)

#     index, stored_chunks = load_vector_database()

#     st.success("Document processed successfully!")

#     question = st.text_input("Ask a question")

#     if question:

#         retrieved = retrieve_chunks(
#             question,
#             index,
#             stored_chunks
#         )

#         context = "\n\n".join(retrieved)

#         answer = generate_answer(
#             question,
#             context
#         )

#         st.subheader("Answer")

#         st.write(answer)

#         with st.expander("Retrieved Context"):

#             for i, chunk in enumerate(retrieved):

#                 st.write(f"### Chunk {i+1}")

#                 st.write(chunk)