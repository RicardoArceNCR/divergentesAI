# Usa una imagen oficial de Python
FROM python:3.10

# Crea un directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de dependencias primero para aprovechar cache
COPY requirements.txt .

# Instala dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el código al contenedor
COPY . .

# Expone el puerto por donde corre FastAPI
EXPOSE 8000

# Comando que corre la app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
