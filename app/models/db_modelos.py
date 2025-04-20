# app/modelos/db_modelos.py
from sqlalchemy import Column, Integer, String, Text, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class ResultadoProcesado(Base):
    __tablename__ = "resultados"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String)
    titulo = Column(String)
    resumen = Column(Text)
    categorias = Column(JSON)  # ej: {"politica": 0.95}
    fecha_procesado = Column(DateTime, default=datetime.utcnow)
