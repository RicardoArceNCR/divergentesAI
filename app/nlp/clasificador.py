import warnings
warnings.filterwarnings("ignore", category=FutureWarning, module="huggingface_hub")

from sentence_transformers import SentenceTransformer, util

modelo = SentenceTransformer("all-MiniLM-L6-v2")

CATEGORIAS = {
    "corrupción": "Este texto trata sobre corrupción política o institucional.",
    "política": "Este texto trata sobre decisiones gubernamentales, partidos políticos o procesos electorales.",
    "violencia": "Este texto menciona represión, asesinatos, uso de la fuerza o violencia policial.",
    "economía": "Este texto trata sobre dinero, finanzas, impuestos o economía del país.",
    "derechos humanos": "Este texto trata sobre violaciones a los derechos fundamentales.",
    "internacional": "Este texto se relaciona con relaciones exteriores o actores internacionales."
}

def clasificar_texto(texto: str, top_n: int = 3) -> dict:
    texto_emb = modelo.encode(texto, convert_to_tensor=True)
    scores = {}
    for categoria, descripcion in CATEGORIAS.items():
        desc_emb = modelo.encode(descripcion, convert_to_tensor=True)
        score = util.cos_sim(texto_emb, desc_emb).item()
        scores[categoria] = round(score, 3)

    return dict(sorted(scores.items(), key=lambda x: x[1], reverse=True)[:top_n])
