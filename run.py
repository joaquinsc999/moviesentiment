from app import create_app
from waitress import serve
from app.config import Config

app = create_app()

if __name__ == '__main__':
    print(f"Iniciando servicio de modelos en el puerto {Config.PORT}")
    serve(app, host='0.0.0.0', port=Config.PORT)
