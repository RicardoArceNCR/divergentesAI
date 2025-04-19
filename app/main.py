from fastapi import FastAPI
from app.rutas.articulos import router as articulos_router
from app.rutas.resumenes import router as resumenes_router
from app.rutas.clasificacion import router as clasificacion_router
from app.rutas.imagenes import router as imagenes_router

app = FastAPI(
    title="DivergenteRAG",
    description="API para análisis editorial automatizado",
    version="0.1.0",
)

app.include_router(articulos_router)
app.include_router(resumenes_router)
app.include_router(clasificacion_router)
app.include_router(imagenes_router)