def clasificar_texto(texto: str) -> dict:
    # Simulación simple basada en palabras clave
    categorias = {
        "politica": ["gobierno", "presidente", "elección", "diputado"],
        "corrupcion": ["soborno", "lavado", "malversación"],
        "derechos_humanos": ["represión", "protesta", "exilio", "presos"],
    }

    resultado = {}
    texto_lower = texto.lower()
    for categoria, palabras in categorias.items():
        resultado[categoria] = sum(p in texto_lower for p in palabras) / len(palabras)

    return resultado
