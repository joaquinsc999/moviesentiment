# app/middleware/error_middleware.py
from flask import jsonify
from app.helpers.errors_helper import AppError
from app.utils import loggers

def register_error_handlers(app):
    @app.errorhandler(AppError)
    def handle_app_error(error):
        # Loguear el error (puedes usar el logger que prefieras)
        loggers.error(f"Error controlado en solicitud: {error.message}")
        response = {
            "status": error.status,
            "message": error.message
        }
        return jsonify(response), error.status_code

    @app.errorhandler(Exception)
    def handle_generic_error(error):
        # Logueamos el error con el traceback para mayor detalle
        loggers.error("Error no controlado en solicitud", error)
        response = {
            "status": "fail",
            "message": "Error inesperado en solicitud"
        }
        return jsonify(response), 500
