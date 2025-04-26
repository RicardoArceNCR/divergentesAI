from sentence_transformers import SentenceTransformer
import json

modelo = SentenceTransformer("all-MiniLM-L6-v2")

def generar_embedding(texto: str) -> list:
    """Devuelve un embedding como lista de floats"""
    return modelo.encode(texto).tolist()

def serializar_embedding(embedding: list) -> str:
    """Convierte la lista de floats a un string JSON"""
    return json.dumps(embedding)

def deserializar_embedding(embedding_str: str) -> list:
    """Convierte el string JSON a lista de floats"""
    return json.loads(embedding_str)
