import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
print("🔐 API Key (inicio parcial):", openai.api_key[:8])

def generar_imagen(prompt: str) -> str:
    """
    Genera una imagen a partir de un prompt usando OpenAI DALL·E.

    Args:
        prompt (str): Texto descriptivo para generar la imagen.

    Returns:
        str: URL de la imagen generada o un placeholder si falla.
    """
    if not prompt or not isinstance(prompt, str):
        raise ValueError("El prompt debe ser un string no vacío.")

    try:
        response = openai.images.generate(
            model="dall-e-3",  # o "dall-e-2" si tu cuenta no tiene acceso
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        return response.data[0].url
    except Exception as e:
        print(f"❌ Error al generar imagen: {e}")
        return "https://via.placeholder.com/1024?text=Error+al+generar+imagen"
if os.getenv("DEBUG") == "1":
    print("🔐 API Key (inicio parcial):", openai.api_key[:8])
