# Makefile para DivergenteRAG

# Variables
VENV=.venv
PYTHON=$(VENV)/bin/python
PIP=$(VENV)/bin/pip
UVICORN=$(VENV)/bin/uvicorn

# Crear entorno virtual e instalar dependencias
init:
	python3.10 -m venv $(VENV)
	$(PIP) install -r requirements.txt

# Ejecutar localmente
dev:
	$(UVICORN) app.main:app --reload

# Ejecutar con Docker
docker:
	docker-compose build --no-cache
	docker-compose up

# Ejecutar pruebas
test:
	$(VENV)/bin/pytest

# Limpiar archivos temporales
clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	rm -rf .pytest_cache

# Activar entorno virtual (manual)
activate:
	@echo "Ejecuta: source $(VENV)/bin/activate"

.PHONY: init dev docker test clean activate
