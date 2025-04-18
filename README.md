# 🧠 DivergenteRAG – Plataforma local de análisis crítico y automatización editorial

**DivergenteRAG** es un sistema local construido con FastAPI que permite analizar artículos web, generar resúmenes automáticos y exponer los resultados mediante endpoints REST. Está diseñado para equipos editoriales que buscan automatizar análisis de contenido y generar materiales con IA de forma crítica, rápida y eficiente.

---

## 📁 Estructura del proyecto

```
DIVERGENTESAI/
├── app/                  # Lógica principal de la API
│   ├── rutas/            # Endpoints organizadosa
│   ├── modelos.py        # Modelos Pydantic
│   ├── resumen.py        # Función de resumen de texto
│   └── main.py           # Entrada de la aplicación FastAPI
├── services/             # Conexiones a OpenAI, prompts, utilidades
├── test/                 # Pruebas automáticas (pytest)
├── Dockerfile            # Imagen base para contenedor
├── docker-compose.yml    # Orquestador de servicios
├── requirements.txt      # Lista de dependencias
└── README.md             # Documentación del proyecto
```

---

## 🚀 Cómo ejecutar el servidor

En entorno local:

```bash
uvicorn app.main:app --reload
```

O usando Docker Compose:

```bash
docker-compose up --build
```

---

## 🔌 Endpoints disponibles

### `GET /articulos?n=5`
Extrae y resume automáticamente los últimos artículos encontrados en la web.

- **Parámetro opcional**: `n` – cantidad de artículos a procesar (por defecto: 5)

📦 **Ejemplo de respuesta:**

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

## 📦 Instalación de dependencias

```bash
pip install -r requirements.txt
```

---

## 🧪 Ejecutar pruebas

```bash
pytest
```

---

## 🛠 Tecnologías clave

- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [OpenAI API](https://platform.openai.com/)
- [Docker](https://www.docker.com/)
- [Pytest](https://docs.pytest.org/)

---

## ✨ Contribuciones

¡Las ideas, sugerencias y mejoras son bienvenidas!  
Podés abrir un issue o enviar un Pull Request. Este proyecto busca crecer con aportes editoriales, técnicos y creativos.

---

## 📫 Contacto

> Ricardo Alberto Arce Aburto  
> [GitHub](https://github.com/RicardoArceNCR)
