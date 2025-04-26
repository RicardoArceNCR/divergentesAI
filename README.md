# DivergenteRAG 2.0

🚀 Sistema de extracción, análisis y recuperación aumentada de información de noticias, utilizando FastAPI, embeddings semánticos y bases vectoriales.

---

## 📙 Descripción

DivergenteRAG permite:
- Realizar scraping automático de sitios de noticias.
- Resumir, clasificar temáticamente y extraer entidades de los textos.
- Generar embeddings semánticos y almacenar los resultados.
- Consultar artículos similares a partir de preguntas.
- Generar imágenes automáticas a partir de prompts (vía OpenAI).

Ideal para proyectos de análisis de medios, reportes automáticos o bases de conocimiento.

---

## 📊 Estructura del Proyecto

```plaintext
app/
 ├── database/          # Bases de datos locales (SQLite y ChromaDB)
 ├── ingestion/         # Scrapers y limpieza de datos
 ├── services/          # NLP, OpenAI, query de vectores
 ├── logic/             # Análisis: resumen, clasificación, entidades
 ├── nlp/               # Modelos spaCy y Sentence-Transformers
 ├── models/            # Pydantic schemas para FastAPI
 ├── routes/            # Endpoints FastAPI organizados por funcionalidad
 └── utils/              # Manejo de errores y logs
```

---

## 🛠️ Instalación Rápida

1. Clona este repositorio:

```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio
```

2. Crea un entorno virtual e instala las dependencias:

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Agrega un archivo `.env` en la raíz del proyecto:

```dotenv
OPENAI_API_KEY=sk-XXXXXXXXXXXXXXXXXXXXXXXXXXX
```

---

## 🚀 Ejecución del Servidor

Lanza la API localmente con:

```bash
uvicorn app.main:app --reload
```

Accede a la documentación interactiva en:
- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- Redocly: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 👁️ Endpoints Principales

| Ruta                  | Método | Descripción |
|:----------------------|:--------|:------------|
| `/articulos`           | GET     | Obtener artículos resumidos con embeddings |
| `/articulos/extendidos`| GET     | Obtener artículos completos |
| `/query`               | POST    | Buscar artículos similares mediante pregunta |
| `/upsert`              | POST    | Insertar manualmente un artículo en ChromaDB |
| `/clasificar`          | POST    | Clasificar un texto por temática |
| `/entidades`           | POST    | Extraer entidades nombradas |
| `/imagen`              | GET     | Generar imagen desde prompt OpenAI |
| `/resumir`             | POST    | Resumir un texto enviado |

---

## 🎓 Tecnologías Usadas

- **FastAPI** — Servidor de aplicaciones
- **SQLAlchemy** — ORM para base de datos SQLite
- **ChromaDB** — Base de datos vectorial local
- **Sentence Transformers** — Embeddings semánticos
- **spaCy** — Extracción de entidades en español
- **OpenAI API** — Generación de imágenes
- **BeautifulSoup4 / Cloudscraper** — Scraping de sitios web

---

## 📆 Planes a Futuro

- Agregar autenticación y usuarios.
- Mejorar el motor de RAG con rerankers locales.
- Dashboard visual para explorar resultados.

---

## 📘 Licencia

Este proyecto es de uso libre para fines educativos y de experimentación. Puedes adaptarlo o expandirlo mencionando el proyecto original.

---

> Creado con ❤️ para el análisis crítico de medios de comunicación.