# 📦 Imagen base liviana y estable
FROM python:3.10-slim

# 🗂️ Directorio de trabajo
WORKDIR /app

# 🛠️ Instala dependencias del sistema necesarias para compilar paquetes
RUN apt-get update && apt-get install -y \
    build-essential gcc g++ git \
    libffi-dev libxml2-dev libxslt1-dev zlib1g-dev \
    libjpeg-dev libopenblas-dev liblapack-dev \
    && rm -rf /var/lib/apt/lists/*

# 📄 Copia dependencias primero para usar cache
COPY requirements-dockers.txt .

# 📦 Instala Python requirements
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements-dockers.txt

# 📁 Copia el resto del código
COPY . .

# 🌐 Expone puerto FastAPI
EXPOSE 8000

# 🚀 Comando default (modo producción)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
