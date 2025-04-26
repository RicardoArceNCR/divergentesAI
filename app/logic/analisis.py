from app.services.scraper_extractor import extraer_contenido
from app.nlp.clasificador import clasificar_texto
from app.nlp.entidades import extraer_entidades
from app.logic.summary import resumir

def procesar_articulo_completo(url: str) -> dict:
    """
    Toma una URL y devuelve un artículo con metadatos, resumen, categorías, entidades y logs de validación.
    """
    print(f"🔍 Procesando: {url}")
    datos = extraer_contenido(url)

    texto = datos.get("texto", "").strip()
    if not texto or len(texto) < 30:
        print(f"❌ Texto vacío o demasiado corto para: {url}")
        return {
            "url": url,
            "error": "Texto vacío o muy corto",
            "datos_raw": datos
        }

    resultado = {
        "titulo": datos.get("titulo", "Sin título"),
        "subtitulo": datos.get("subtitulo", ""),
        "url": url,
        "autor": datos.get("autor", ""),
        "fecha": datos.get("fecha", ""),
        "texto": texto
    }

    try:
        resumen = resumir(texto)
        resultado["resumen"] = resumen if resumen != "string" else ""
        print(f"📝 Resumen generado: {resumen[:80]}...")
    except Exception as e:
        resultado["resumen"] = ""
        print(f"⚠️ Error al generar resumen: {e}")

    try:
        categorias = clasificar_texto(texto)
        resultado["categorias"] = categorias
        print(f"📊 Categorías: {categorias}")
    except Exception as e:
        resultado["categorias"] = {}
        print(f"⚠️ Error al clasificar texto: {e}")

    try:
        entidades = extraer_entidades(texto)
        resultado["entidades"] = entidades
        print(f"🏷️ Entidades: {entidades}")
    except Exception as e:
        resultado["entidades"] = {}
        print(f"⚠️ Error al extraer entidades: {e}")

    return resultado
