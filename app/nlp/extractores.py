import spacy
nlp = spacy.load("es_core_news_md")

def extraer_entidades(texto: str) -> dict:
    doc = nlp(texto)
    entidades = {"PERSONA": [], "ORG": [], "LOC": []}
    for ent in doc.ents:
        if ent.label_ in entidades:
            entidades[ent.label_].append(ent.text)
    return {k: list(set(v)) for k, v in entidades.items()}