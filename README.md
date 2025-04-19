# 🧠 DivergenteRAG – Plataforma de análisis crítico y automatización editorial

Sistema local con FastAPI que analiza artículos, resume contenido y expone endpoints para uso editorial y visualización automatizada.

---

## 🗂️ Estructura del proyecto

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

---

## 🐳 Ejecutar con Docker

```bash
# Levantar entorno
docker-compose build --no-cache
docker-compose up
```

---

## 🧪 Ejecutar pruebas

```bash
pytest
```

---

## 🔐 Variables de entorno

Crear archivo `.env` basado en `.env.example`:

```env
OPENAI_API_KEY=tu_clave_openai
ENV=development
PORT=8000
```

---

## 📦 Comandos con Make

Este proyecto incluye un `Makefile` para automatizar tareas comunes:

| Comando | Descripción |
|--------|-------------|
| `make init` | Crea entorno virtual e instala dependencias |
| `make dev` | Ejecuta el servidor local con FastAPI |
| `make docker` | Compila y levanta los contenedores con Docker |
| `make test` | Ejecuta pruebas con `pytest` |
| `make clean` | Elimina cachés y carpetas temporales |
| `make activate` | Muestra cómo activar el entorno virtual |

> Asegúrate de tener `make` instalado en tu sistema (Linux/macOS lo incluyen por defecto, en Windows se puede usar [GnuWin](http://gnuwin32.sourceforge.net/packages/make.htm) o WSL).