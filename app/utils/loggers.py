import logging
from flask import current_app

# Filtro personalizado para aceptar solo registros de un nivel específico
class LevelFilter(logging.Filter):
    def __init__(self, level):
        super().__init__()
        self.level = level

    def filter(self, record):
        return record.levelno == self.level

def configure_loggers(app):
    # Limpiamos los handlers por defecto de app.logger
    app.logger.handlers.clear()
    
    # --- Handler para INFO ---
    info_handler = logging.StreamHandler()
    info_handler.setLevel(logging.INFO)
    info_handler.addFilter(LevelFilter(logging.INFO))
    info_formatter = logging.Formatter(
        "\n===== INFO =====\n%(asctime)s - %(levelname)s - %(message)s\n================",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    info_handler.setFormatter(info_formatter)
    
    # --- Handler para WARNING ---
    warning_handler = logging.StreamHandler()
    warning_handler.setLevel(logging.WARNING)
    warning_handler.addFilter(LevelFilter(logging.WARNING))
    warning_formatter = logging.Formatter(
        "\n===== WARNING =====\n%(asctime)s - %(levelname)s - %(message)s\n===================",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    warning_handler.setFormatter(warning_formatter)
    
    # --- Handler para ERROR ---
    error_handler = logging.StreamHandler()
    error_handler.setLevel(logging.ERROR)
    error_handler.addFilter(LevelFilter(logging.ERROR))
    error_formatter = logging.Formatter(
        "\n===== ERROR =====\n%(asctime)s - %(levelname)s - %(message)s\n=================",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    error_handler.setFormatter(error_formatter)
    
    # Agregamos los handlers al logger de la aplicación
    app.logger.addHandler(info_handler)
    app.logger.addHandler(warning_handler)
    app.logger.addHandler(error_handler)
    
    # Ajustamos el nivel global del logger para capturar todos los mensajes
    app.logger.setLevel(logging.DEBUG)


def error(message, data=None):
    if data:
        current_app.logger.error(f"{message} - Data: {data}")
    else:
        current_app.logger.error(message)

def info(message, data=None):
    if data:
        current_app.logger.info(f"{message} - Data: {data}")
    else:
        current_app.logger.info(message)

def warning(message, data=None):
    if data:
        current_app.logger.warning(f"{message} - Data: {data}")
    else:
        current_app.logger.warning(message)
