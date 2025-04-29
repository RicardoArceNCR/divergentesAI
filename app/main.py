# app/main.py
from fastapi import FastAPI
from app.routes import articles, summaries, classification_router
from app.routes import query_router, upsert_router, resumen_router
from app.routes import articulos_crawler

def create_app() -> FastAPI:
    app = FastAPI(title="DivergenteRAG 2.0")

    # Routers antiguos (ya en tu sistema)
    app.include_router(articles.router)
    app.include_router(summaries.router)
    app.include_router(classification_router.router)

    # Routers nuevos para RAG
    app.include_router(query_router.router)
    app.include_router(upsert_router.router)
    app.include_router(resumen_router.router)
    app.include_router(articulos_crawler.router)

    return app

app = create_app()