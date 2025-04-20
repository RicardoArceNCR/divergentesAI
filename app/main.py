from fastapi import FastAPI
from app.routes.articles import router as articles_router
from app.routes.summaries import router as resumenes_router
from app.routes.classification import router as classification_router
from app.routes.images import router as imagenes_router

from app.logic.summary import resumir
from app.services.openai_client import generar_imagen

app = FastAPI(
    title="DivergenteRAG",
    description="API para análisis editorial automatizado",
    version="0.1.0",
)

app.include_router(articles_router)
app.include_router(resumenes_router)
app.include_router(classification_router)
app.include_router(imagenes_router)
