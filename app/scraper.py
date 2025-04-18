import requests
from bs4 import BeautifulSoup

def obtener_urls_home(url="https://www.divergentes.com"):
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; RicardoBot/1.0)"
    }

    response = requests.get(url, headers=headers, allow_redirects=True, timeout=10)
    response.raise_for_status()  # lanza error si la respuesta es 4xx o 5xx

    soup = BeautifulSoup(response.text, "html.parser")
    enlaces = [a['href'] for a in soup.find_all("a", href=True) if "/202" in a['href']]
    return list(set(enlaces))


def extraer_contenido(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    titulo = soup.find("h1").get_text(strip=True) if soup.find("h1") else ""
    parrafos = soup.find_all("p")
    cuerpo = "\n".join([p.get_text(strip=True) for p in parrafos])

    return {
        "titulo": titulo,
        "url": url,
        "texto": cuerpo,
        "autor": "",     # Se puede mejorar si Divergentes lo estructura
        "fecha": ""      # Igual para la fecha
    }

