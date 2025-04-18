# Usa una imagen oficial de Python
FROM python:3.10

# Crea un directorio de trabajo dentro del contenedor
WORKDIR /app

# Requisitos del sistema para compilar dependencias pesadas
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    g++ \
    libffi-dev \
    libxml2-dev \
    libxslt1-dev \
    zlib1g-dev \
    libjpeg-dev \
    libopenblas-dev \
    liblapack-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copia el archivo de dependencias primero para aprovechar cache de Docker
COPY requirements-dockers.txt .

# Instala dependencias
RUN pip install --no-cache-dir -r requirements-dockers.txt

# Copia el resto del proyecto al contenedor
COPY . .

# Expone el puerto por donde corre FastAPI
EXPOSE 8000

# Comando por defecto para ejecutar la API
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
