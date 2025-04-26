# DivergenteRAG

Sistema de análisis editorial automatizado con IA para medios independientes.

## 📦 Estructura Principal

- **Scraping:** Recolecta artículos de medios registrados (Divergentes, Confidencial, etc.).
- **Ingestión:** Limpieza y procesamiento básico de los artículos.
- **Procesamiento NLP:** Clasificación, extracción de entidades, creación de embeddings semánticos.
- **Análisis Crítico:** Generación de resúmenes editoriales y análisis asistido por IA.
- **Exposición API:** Endpoints para consultar resultados, resúmenes, clasificaciones y embeddings.

## 🛠️ Tecnologías

- **Python 3.10+**
- **FastAPI**
- **Sentence Transformers**
- **OpenAI API**
- **SQLAlchemy**
- **Docker**

## 📂 Estructura de carpetas

```plaintext
app/
  ├── scrapers/               # Scrapers específicos por medio
  ├── services/
  │   ├── ingestion_pipeline.py
  │   ├── embedding_utils.py
  │   └── coordinador_scrapers.py
  ├── nlp/
  │   ├── embedding.py
  │   ├── clasificador.py
  │   └── entidades.py
  ├── logic/
  │   └── analisis.py
  ├── routes/
  │   ├── articles.py
  │   ├── classification_router.py
  │   └── resultados.py
  ├── models/
  │   ├── article.py
  │   ├── classification.py
  │   └── db_modelos.py
  ├── utils/
  │   ├── logs.py
  │   └── schemas.py
  ├── database.py
  ├── main.py

🚀 Cómo levantar el proyecto

# 1. Clonar el repositorio
git clone https://github.com/tuusuario/tu-repo.git
cd tu-repo

# 2. Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar API
uvicorn app.main:app --reload

🧠 Funcionalidades principales
Scrapeo automático de medios.

Clasificación editorial basada en embeddings.

Extracción de entidades clave.

Generación de resúmenes críticos.

API REST para consulta de resultados.

📜 Licencia
MIT License.

---

### 🚀 ¿Te gustaría que además te prepare:
- Un esquema `.drawio` limpio basado en esta propuesta ✅
- O un diagrama `.svg` / `.png` listo para meter al README ✅

¿Te lo preparo? 🔥  
(Si quieres, puedo incluirlo en estilo profesional de arquitectura SaaS) 🚀