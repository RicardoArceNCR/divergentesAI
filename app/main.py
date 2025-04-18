from fastapi import FastAPI
from app.rutas.articulos import router as articulos_router

app = FastAPI()

app.include_router(articulos_router)
