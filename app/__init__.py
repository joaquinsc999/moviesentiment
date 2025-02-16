# app/__init__.py
from flask import Flask
from app.config import Config
from app.routes import register_routes
from app.middlewares.errors_handler import register_error_handlers
from app.utils.loggers import configure_loggers

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    #loggers con formato estandarizado
    configure_loggers(app)
    
    # Registrar las rutas
    register_routes(app)
    
    # Registrar el middleware de errores
    register_error_handlers(app)
    
    return app
