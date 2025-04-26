# DivergenteRAG API

**Análisis editorial automatizado para medios independientes**

---

## 📊 Descripción

DivergenteRAG es una API desarrollada con **FastAPI** que permite:
- Ingesta automatizada de artículos de medios como Divergentes, La Prensa y Confidencial.
- Resumen automático de contenidos.
- Clasificación semántica de textos.
- Extracción de entidades nombradas (personas, organizaciones, lugares).
- Generación de embeddings y vectores semánticos.
- Generación de imágenes desde prompts.

Todo está organizado de manera modular, escalable y segura.

---

## 🔄 Instalación local

1. Clona el repositorio:

```bash
https://github.com/RicardoArceNCR/divergentesAI.git
cd divergentesAI
```

2. Crea y activa un entorno virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

4. Instala el modelo de SpaCy en español:

```bash
python -m spacy download es_core_news_sm
```

---

## 🔒 Variables de entorno

Crea un archivo `.env` en la raíz basado en `.env.example`:

```bash
cp .env.example .env
```

Completa:

```bash
OPENAI_API_KEY=tu-api-key-de-openai
ENV=development
PORT=8000
```

**Importante:** No subas nunca `.env` a GitHub.

---

## 🚀 Cómo levantar la API

Levantar localmente en modo desarrollo:

```bash
uvicorn app.main:app --reload
```

Acceder a la documentación interactiva:

- [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) (Swagger UI)
- [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) (Redoc)

---

## 🔢 Ingesta de artículos

Para correr la ingesta automática de medios:

```bash
python app/ingestion/ingestion_pipeline.py
```

Esto guardará los artículos procesados en:

```bash
/data/processed/
```

---

## 🔧 Endpoints principales

| Método | Ruta | Descripción |
|:-------|:-----|:-------------|
| GET | `/articulos` | Artículos resumidos con embedding |
| GET | `/articulos/extendidos` | Artículos extendidos con más metadatos |
| GET | `/articulos/analizados` | Artículos analizados con resumen, entidades, categorías |
| POST | `/resumir` | Genera resumen de un texto |
| POST | `/clasificar` | Clasifica texto por temática |
| POST | `/entidades` | Extrae entidades (PERSONA, ORG, LOC) |
| GET | `/imagen?prompt=...` | Genera imagen DALL-E desde texto |
| GET | `/logs/resumen` | Consulta últimos artículos analizados |

---

## 🛡️ Seguridad

- `.env` está en `.gitignore`, protegido.
- No subir nunca llaves de API a GitHub.
- Al trabajar en colaboración, usar `.env.example` como plantilla.

---

## 📊 Tecnologías usadas

- **FastAPI**
- **Pydantic**
- **SQLAlchemy** (SQLite embedido)
- **SpaCy** (NLP en español)
- **Sentence-Transformers** (Embeddings)
- **OpenAI API** (Generación de imágenes)
- **BeautifulSoup** (Web scraping)

---

## 👩‍💼 Contribución

1. Haz un fork
2. Crea una rama nueva: `git checkout -b feature/tu-feature`
3. Commitea tus cambios: `git commit -m "feat: tu descripción"`
4. Haz push a la rama: `git push origin feature/tu-feature`
5. Abre un Pull Request

---

# 🎉 Gracias por apoyar el periodismo independiente.
