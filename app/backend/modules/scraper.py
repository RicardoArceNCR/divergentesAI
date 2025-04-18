def obtener_urls_home() -> list[str]:
    # Aquí va el scraping para sacar URLs de la homepage
    return ["https://ejemplo.com/articulo1", "https://ejemplo.com/articulo2"]

def extraer_contenido(url: str) -> dict:
    # Aquí va el scraping de un artículo específico
    return {
        "titulo": "Ejemplo de Título",
        "texto": "Contenido del artículo...",
        "autor": "Nombre del autor",
        "fecha": "2025-04-16"
    }
