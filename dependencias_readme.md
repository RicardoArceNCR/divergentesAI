
### 📦 Gestión de dependencias

Este proyecto utiliza distintos archivos `requirements` para separar el entorno de desarrollo del entorno de producción:

| Archivo | Uso | Descripción |
|--------|-----|-------------|
| `requirements.txt` | 🔧 Desarrollo local | Incluye librerías necesarias para desarrollo, pruebas y ejecución en entornos no Docker. Útil para trabajar directamente en tu máquina. |
| `requirements-dockers.txt` | 🐳 Producción en Docker | Optimizado para ambientes Linux (x86_64) dentro de contenedores. Incluye versiones compatibles de `torch` y `torchvision` para CPU. Ideal para despliegue. |

#### ▶️ Instalación local
```bash
pip install -r requirements.txt
```

#### 🐳 Instalación en Docker (automático)
Tu `Dockerfile` utiliza el archivo `requirements-dockers.txt` para instalar solo lo necesario en producción:

```dockerfile
COPY requirements-dockers.txt .
RUN pip install --no-cache-dir -r requirements-dockers.txt
```
