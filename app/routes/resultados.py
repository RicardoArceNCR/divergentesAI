# app/rutas/resultados.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.db_modelos import ResultadoProcesado
from app.schemas import ResultadoCreate  # lo definimos abajo

router = APIRouter()

@router.post("/resultados")
def guardar_resultado(data: ResultadoCreate, db: Session = Depends(get_db)):
    nuevo = ResultadoProcesado(**data.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.get("/resultados")
def listar_resultados(db: Session = Depends(get_db)):
    return db.query(ResultadoProcesado).all()
