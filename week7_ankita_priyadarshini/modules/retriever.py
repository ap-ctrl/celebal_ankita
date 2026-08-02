import faiss
import pickle

from sentence_transformers import SentenceTransformer
from config import TOP_K

model = SentenceTransformer("all-MiniLM-L6-v2")


def load_vector_database():

    index = faiss.read_index("vector_db/faiss_index.bin")

    with open("vector_db/chunks.pkl", "rb") as f:
        chunks = pickle.load(f)

    return index, chunks


def retrieve_chunks(question, index, chunks):

    question_embedding = model.encode([question])

    distances, indices = index.search(question_embedding, TOP_K)

    retrieved_chunks = []

    for idx in indices[0]:
        retrieved_chunks.append(chunks[idx])

    return retrieved_chunks


# import faiss
# import pickle

# from sentence_transformers import SentenceTransformer
# from config import TOP_K

# # Load embedding model
# model = SentenceTransformer("all-MiniLM-L6-v2")


# def retrieve_chunks(question):
#     """
#     Retrieve the most relevant chunks for a user question.
#     """

#     # Load FAISS index
#     index = faiss.read_index("vector_db/faiss_index.bin")

#     # Load stored chunks
#     with open("vector_db/chunks.pkl", "rb") as f:
#         chunks = pickle.load(f)

#     # Convert question into embedding
#     question_embedding = model.encode([question])

#     # Search
#     distances, indices = index.search(question_embedding, TOP_K)

#     # Retrieve chunks
#     retrieved_chunks = []

#     for idx in indices[0]:
#         retrieved_chunks.append(chunks[idx])

#     return retrieved_chunks