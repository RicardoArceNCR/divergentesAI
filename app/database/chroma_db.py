import chromadb
from chromadb.config import Settings

try:
    chroma_client = chromadb.Client(
        Settings(
            chroma_db_impl="duckdb+parquet",
            persist_directory="./data/chromadb"
        )
    )
except Exception as e:
    chroma_client = None
    print(f"⚠️ Error inicializando Chroma: {e}")

def get_or_create_collection(collection_name="articulos"):
    if chroma_client is None:
        raise RuntimeError("Chroma Client no está disponible.")
    return chroma_client.get_or_create_collection(name=collection_name)

def insert_documents(documents: list, ids: list, metadatas: list):
    collection = get_or_create_collection()
    collection.add(documents=documents, ids=ids, metadatas=metadatas)
    chroma_client.persist()

def query_similar_documents(query_text: str, n_results: int = 5):
    collection = get_or_create_collection()
    results = collection.query(
        query_texts=[query_text],
        n_results=n_results,
        include=["documents", "metadatas"]
    )
    return results
