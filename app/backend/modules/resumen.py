from summarizer import Summarizer
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("mrm8488/bert-base-spanish-wwm-cased-finetuned-spa-squad2-es")
model = AutoModel.from_pretrained("mrm8488/bert-base-spanish-wwm-cased-finetuned-spa-squad2-es")
custom_model = Summarizer(custom_model=model, custom_tokenizer=tokenizer)

def resumir_con_modelo(texto, max_frases=3):
    return custom_model(texto, num_sentences=max_frases)

def resumen_basico(texto: str) -> str:
    return texto[:200] + "..." if len(texto) > 200 else texto