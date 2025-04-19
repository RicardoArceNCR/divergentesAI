from summarizer import Summarizer
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("mrm8488/bert-base-spanish-wwm-cased-finetuned-spa-squad2-es")
model = AutoModel.from_pretrained("mrm8488/bert-base-spanish-wwm-cased-finetuned-spa-squad2-es")
custom_model = Summarizer(custom_model=model, custom_tokenizer=tokenizer)

def resumir(texto, max_frases=3):
    return custom_model(texto, num_sentences=max_frases)

from app.__version__ import __version__
print(f"🚀 Iniciando DivergenteRAG v{__version__}")

