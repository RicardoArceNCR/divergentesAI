🧠 DivergenteRAG

DivergenteRAG es un sistema modular para procesamiento, análisis editorial automatizado y generación crítica de contenido periodístico, diseñado para medios independientes y proyectos de investigación. Usa técnicas de NLP, embeddings semánticos y generación con modelos como OpenAI para crear resúmenes, clasificaciones y estructuras editoriales a partir de scraping inteligente.

📁 Estructura del Proyecto

app/
├── ingestion/                 # Módulo de scraping y limpieza
│   ├── ingestion_pipeline.py
│   ├── cleanners.py
│   └── coordinador_scraper.py
│       └── scrapers/
│           ├── scraper_template.py
│           ├── divergentes_scraper.py
│           └── confidencial.py
│
├── logic/                     # Núcleo de procesamiento editorial
│   ├── analisis.py            # Orquesta resumen + clasificación + entidades
│   ├── classification.py
│   └── embedding.py
│
├── services/                  # Utilidades para generación, APIs y embeddings
│   ├── openai_client.py       # Invoca OpenAI
│   ├── prompt_utils.py        # Construye prompts
│   ├── summaries.py           # Transforma respuestas en textos editoriales
│   └── embedding_utils.py     # Coordina embeddings locales o remotos
│
├── nlp/                       # Modelos NLP locales
│   ├── embedding.py
│   ├── entidades.py
│   └── clasificador.py
│
├── models/                    # Definición de modelos Pydantic y DB
│   ├── article.py
│   ├── classification.py
│   ├── db_modelos.py
│   └── resultados.py
│
├── routes/                    # Endpoints FastAPI
│   ├── articles.py
│   ├── classification_router.py
│   └── resultados.py
│
├── utils/
│   └── logs.py                # Logs y helpers
│
├── database/
│   ├── database.py
│   └── schemas.py
│
└── main.py                    # Inicia FastAPI y monta rutas

⚙️ Instalación

Clona el repositorio:

git clone https://github.com/ricardoarceNCR/divergentesAI.git
cd divergentesAI

Crea un entorno virtual e instala dependencias:

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Crea el archivo .env con tus credenciales:

OPENAI_API_KEY=tu_api_key

🚀 Ejecutar en desarrollo

uvicorn app.main:app --reload

Para probar los endpoints, accede a: http://localhost:8000/docs

🧰 Funcionalidades clave

👷️ Scrapers especializados para medios como Divergentes y Confidencial

🧼 Limpieza automatizada del contenido

🧠 Clasificación semántica, entidades y resumen vía analisis.py

📦 Generación editorial vía OpenAI y módulos locales de NLP

🌟 Embeddings para futuras búsquedas y RAG (Retrieval-Augmented Generation)

🔌 API REST completa con rutas documentadas

🧪 Pruebas

pytest tests/

(Puedes agregar cobertura con coverage si se requiere producción futura.)

🔭 Roadmap (Propuesto)