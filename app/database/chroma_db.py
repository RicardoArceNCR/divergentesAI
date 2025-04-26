# app/database/chroma_db.py
import chromadb
from chromadb.config import Settings

# Configuración para que guarde la base localmente
chroma_client = chromadb.Client(
    Settings(
        chroma_db_impl="duckdb+parquet",
        persist_directory="./data/chromadb"  # Carpeta donde se guardará tu base
    )
)

# Crear o acceder a una colección
def get_or_create_collection(collection_name="articulos"):
    collection = chroma_client.get_or_create_collection(name=collection_name)
    return collection

# Insertar documentos nuevos
def insert_documents(documents: list, ids: list, metadatas: list):
    """
    documents: lista de textos
    ids: lista de IDs únicos
    metadatas: lista de diccionarios de metadatos (opcional pero recomendado)
    """
    collection = get_or_create_collection()
    collection.add(
        documents=documents,
        ids=ids,
        metadatas=metadatas
    )
    chroma_client.persist()  # Guarda cambios

# Buscar documentos similares
def query_similar_documents(query_text: str, n_results: int = 5):
    collection = get_or_create_collection()
    results = collection.query(
        query_texts=[query_text],
        n_results=n_results,
        include=["documents", "metadatas"]
    )
    return results
