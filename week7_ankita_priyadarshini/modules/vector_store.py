import faiss
import pickle
import numpy as np


def save_vectors(embeddings, chunks):
    """
    Store embeddings in FAISS
    and save text chunks separately.
    """

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(np.array(embeddings))

    faiss.write_index(index, "vector_db/faiss_index.bin")

    with open("vector_db/chunks.pkl", "wb") as f:
        pickle.dump(chunks, f)

    print("Vector database saved successfully!")