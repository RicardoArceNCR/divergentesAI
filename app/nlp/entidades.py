import spacy

nlp = spacy.load("es_core_news_sm")

def extraer_entidades(texto: str) -> list:
    doc = nlp(texto)
    return [{"texto": ent.text, "etiqueta": ent.label_} for ent in doc.ents]
