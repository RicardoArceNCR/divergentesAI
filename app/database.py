# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.db_modelos import Base  # este es el que define la tabla

SQLALCHEMY_DATABASE_URL = "sqlite:///./basedatos.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Esta línea crea las tablas si no existen
Base.metadata.create_all(bind=engine)
