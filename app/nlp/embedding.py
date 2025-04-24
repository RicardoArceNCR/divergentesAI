from sentence_transformers import SentenceTransformer
import json

modelo = SentenceTransformer("all-MiniLM-L6-v2")

def generar_embedding(texto: str) -> list:
    return modelo.encode(texto).tolist()

def serializar_embedding(embedding: list) -> str:
    return json.dumps(embedding)

def deserializar_embedding(embedding_str: str) -> list:
    return json.loads(embedding_str)
