import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

def extraer_contenido(url: str) -> dict:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    dominio = urlparse(url).netloc

    def texto_de(selector, attr=None):
        el = soup.select_one(selector)
        if el:
            return el.get(attr) if attr else el.get_text(strip=True)
        return ""

    def extraer_links(externos=False):
        links = []
        for a in soup.find_all("a", href=True):
            href = a["href"]
            if externos:
                if dominio not in href and href.startswith("http"):
                    links.append(href)
            else:
                if dominio in href or href.startswith("/"):
                    links.append(urljoin(url, href))
        return list(set(links))

    def extraer_colores():
        colores = set()
        for tag in soup.find_all(style=True):
            estilo = tag["style"]
            for parte in estilo.split(";"):
                if "color" in parte:
                    try:
                        colores.add(parte.split(":")[1].strip())
                    except IndexError:
                        continue
        return list(colores)

    def extraer_documentos():
        return [a["href"] for a in soup.find_all("a", href=True) if any(a["href"].endswith(ext) for ext in [".pdf", ".docx", ".xlsx"])]

    def extraer_apis():
        return [a["href"] for a in soup.find_all("a", href=True) if "api" in a["href"]]

    def extraer_anuncios():
        return [div.text.strip() for div in soup.find_all(True, class_=lambda c: c and "ad" in c.lower())]

    titulo = texto_de("h1")
    subtitulo = texto_de("h2")
    autor = texto_de(".author") or texto_de('[name=author]', attr="content")
    fecha = texto_de("time", attr="datetime") or texto_de("meta[name=date]", attr="content")
    cuerpo = "\n".join([p.get_text(strip=True) for p in soup.find_all("p")])

    return {
        "titulo": titulo,
        "subtitulo": subtitulo,
        "autor": autor,
        "fecha": fecha,
        "texto": cuerpo,
        "url": url,
        "links_relacionados": extraer_links(externos=False),
        "links_externos": extraer_links(externos=True),
        "documentos": extraer_documentos(),
        "apis": extraer_apis(),
        "anuncios": extraer_anuncios(),
        "colores": extraer_colores()
    }
