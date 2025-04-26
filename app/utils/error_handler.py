# app/utils/error_handler.py
import logging

logger = logging.getLogger(__name__)

def manejar_error(mensaje: str, error: Exception):
    logger.error(f"{mensaje} - {str(error)}")
