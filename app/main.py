from fastapi import FastAPI

from app.routes.articles import router as articles_router
from app.routes.summaries import router as resumenes_router
from app.routes.classification_router import router as classification_router  # ✅ corregido
from app.routes.images import router as imagenes_router
from app.routes import analysis
from app.routes.logs import router as logs_router



from app.logic.summary import resumir
from app.services.openai.openai_client import generar_imagen

app = FastAPI(
    title="DivergenteRAG",
    description="API para análisis editorial automatizado",
    version="0.1.0",
)

# Registro de rutas
app.include_router(articles_router)
app.include_router(resumenes_router)
app.include_router(classification_router)
app.include_router(imagenes_router)
app.include_router(analysis.router)
app.include_router(logs_router)


from fastapi import FastAPI
from app.routes import analysis, articles, classification_router, summaries

def create_app() -> FastAPI:
    app = FastAPI(title="Tu API Mamadísima")
    
    app.include_router(analysis.router)
    app.include_router(articles.router)
    app.include_router(classification_router.router)
    app.include_router(summaries.router)

    return app

app = create_app()
