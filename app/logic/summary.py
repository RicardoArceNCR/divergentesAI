# app/logic/summary.py

def resumir(texto: str) -> str:
    # Esta es una versión simplificada para pruebas
    return texto[:300] + "..." if len(texto) > 300 else texto
