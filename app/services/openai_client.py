
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
print("🔐 API Key (inicio parcial):", os.getenv("OPENAI_API_KEY")[:8])

def generar_imagen(prompt: str) -> str:
    response = openai.images.generate(
        model="dall-e-3",  # o "dall-e-2" si tu cuenta no tiene acceso
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    return response.data[0].url







