# 🧠 DivergenteRAG – Plataforma de análisis crítico

**DivergenteRAG** es un sistema local basado en FastAPI que analiza artículos web, resume su contenido y expone resultados a través de un endpoint REST. Diseñado para uso editorial, análisis automatizado y generación de contenido con IA.

---

## 📁 Estructura del Proyecto

```
DIVERGENTESAI/
├── app/                  # Código principal de la API
│   ├── rutas/            # Endpoints organizados
│   ├── modelos.py        # Modelos Pydantic
│   ├── resumen.py        # Lógica de resumen
│   └── main.py           # Punto de entrada de FastAPI
├── services/             # Servicios externos (OpenAI, prompts, etc.)
├── test/                 # Pruebas automáticas con pytest
├── Dockerfile            # Imagen Docker
├── docker-compose.yml    # Configuración de contenedor
├── requirements.txt      # Dependencias del proyecto
└── README.md             # Documentación (¡este archivo!)
```

---

## 🚀 Ejecutar el servidor

```bash
uvicorn app.main:app --reload
```

---

## 🔌 Endpoints principales

- `GET /articulos?n=5`  
  Extrae, resume y devuelve los últimos artículos analizados.  
  **Parámetro opcional**: `n` → número de artículos a procesar.

Ejemplo de respuesta:

```json
[
  {
    "titulo": "Título del artículo",
    "resumen": "Texto resumido del artículo",
    "url": "https://ejemplo.com/articulo",
    "autor": "Nombre del autor",
    "fecha": "2025-04-17"
  }
]
```

---

## 🧪 Correr tests

```bash
pytest
```

---

## 📦 Requisitos

Instalación de dependencias:

```bash
pip install -r requirements.txt
```

---

## 🛠 Tecnologías utilizadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [OpenAI API](https://platform.openai.com/)
- [Docker](https://www.docker.com/)
- [Pytest](https://docs.pytest.org/)

---

## ✨ Contribuciones

¡Las contribuciones son bienvenidas! Podés enviar un PR o abrir un issue para mejoras o sugerencias.
