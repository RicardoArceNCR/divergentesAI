# 🧠 DivergenteRAG – Plataforma de análisis crítico y automatización editorial

Sistema local con FastAPI que analiza artículos, resume contenido y expone endpoints para uso editorial y visualización automatizada.

---

## 📁 Estructura del proyecto

- `app/` – Código principal (routers, modelos, servicios)
- `services/` – Módulos auxiliares para IA, scraping, etc.
- `test/` – Tests automáticos con Pytest
- `requirements.txt` – Dependencias locales
- `requirements-dockers.txt` – Dependencias para Docker
- `docker-compose.yml` – Contenedor para ejecución completa
- `Dockerfile` – Imagen base optimizada
- `.venv/` – Entorno virtual local (no se sube a GitHub)

---

## 🚀 Ejecutar en entorno local

```bash
# Crear entorno virtual con Python 3.10
python3.10 -m venv .venv
source .venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Levantar servidor
uvicorn app.main:app --reload
```

Accedé a `http://localhost:8000/docs` para probar los endpoints.

---

## 🐳 Ejecutar con Docker

```bash
docker-compose build --no-cache
docker-compose up
```

La API se levantará en `http://localhost:8000`.

> Si necesitás detenerla:
```bash
docker-compose down
```

---

## 🧪 Testing (opcional)

```bash
pytest
```

---

## 🧠 Funcionalidades actuales

- Resumen automático con BERT
- Cliente OpenAI para generación
- API REST en FastAPI
- Arquitectura modular
