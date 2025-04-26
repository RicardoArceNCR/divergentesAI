# app/services/rag_query_service.py
from app.database.chroma_db import insert_documents, query_similar_documents
from typing import List

def agregar_articulo_a_chroma(titulo: str, texto: str, url: str):
    """
    Inserta un nuevo artículo en ChromaDB.
    """
    document = texto
    id_unico = url  # Asumimos que el URL es único
    metadata = {"titulo": titulo, "url": url}

    insert_documents(
        documents=[document],
        ids=[id_unico],
        metadatas=[metadata]
    )
    return {"mensaje": "Artículo agregado exitosamente."}

def buscar_articulos_similares(pregunta: str, n: int = 5) -> List[dict]:
    """
    Busca artículos similares a la pregunta planteada.
    """
    resultados = query_similar_documents(query_text=pregunta, n_results=n)

    documentos = resultados.get("documents", [[]])[0]
    metadatos = resultados.get("metadatas", [[]])[0]

    respuesta = []
    for doc, meta in zip(documentos, metadatos):
        respuesta.append({
            "titulo": meta.get("titulo", "Sin título"),
            "url": meta.get("url", "Desconocido"),
            "fragmento": doc[:500] + "..." if len(doc) > 500 else doc
        })

    return respuesta
