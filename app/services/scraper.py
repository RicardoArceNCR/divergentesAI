import requests
from bs4 import BeautifulSoup

def obtener_urls_home(url="https://www.divergentes.com"):
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; RicardoBot/1.0)"
    }
    response = requests.get(url, headers=headers, allow_redirects=True)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    enlaces = [a['href'] for a in soup.find_all("a", href=True)]
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
        "autor": "",  # Se puede mejorar si Divergentes lo estructura
        "fecha": ""   # Igual para la fecha
    }
