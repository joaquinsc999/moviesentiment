# app/errors.py
class AppError(Exception):
    def __init__(self, message, status_code=500):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        # Si el status code comienza con 4, se considera un fallo del cliente ("fail"), sino error.
        self.status = 'fail' if str(status_code).startswith('4') else 'error'
        self.is_operational = True  # Indicamos que es un error que controlamos
