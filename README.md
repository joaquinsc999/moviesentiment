# IMDB Sentiment API

Este proyecto implementa una API que analiza el sentimiento de reseñas (reviews) de películas usando un modelo entrenado de TensorFlow. La API toma un texto de entrada y devuelve una predicción binaria (positivo/negativo) junto con un nivel de confianza.

## Características

- **API RESTful** desarrollada con Flask.
- Carga de modelos y preprocesamiento con TensorFlow.
- Capa `TextVectorization` para transformar el texto en secuencias.
- Serialización del vectorizer mediante Pickle.
- Servido en producción con Waitress.
- Soporte para CORS y configuración a través de variables de entorno.

## Requisitos

- Python 3.11 o superior.
- TensorFlow 2.x.
- Flask, Flask-Cors, python-dotenv, waitress.
- Las dependencias completas se encuentran en el archivo `pyproject.toml`.

## Instalación

1. **Clonar el repositorio:**

    ```bash
    git clone https://github.com/tu_usuario/tu_repositorio.git
    cd tu_repositorio
    ```

2. **Crear y activar un entorno virtual:**

    En Linux o macOS:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

    En Windows:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3. **Instalar las dependencias:**

    Si usas pip:
    ```bash
    pip install -r requirements.txt
    ```
    *Nota: Si usas Poetry u otro gestor de dependencias, sigue las instrucciones propias de esa herramienta.*

4. **Colocar los modelos:**

    - Guarda el modelo entrenado en la ruta: `app/models/sentiment_model.keras`.
    - Guarda la configuración del vectorizer en: `app/models/vectorizer_config_3.pkl` (se asume que contiene una tupla `(config, _, vocab)`).

## Uso

Para iniciar la aplicación en modo desarrollo:
```bash
flask run
```

La API se ejecutará en `http://localhost:5000`. Puedes probar el endpoint de predicción enviando una solicitud, por ejemplo:

```bash
curl -X POST http://localhost:5000/sentiment \
  -H "Content-Type: application/json" \
  -d '{"text": "Esta película es increíble"}'
```

Respuesta esperada:

```json
{
  "sentiment": "positive",
  "confidence": 0.93
}
```

## Uso con Docker

El proyecto incluye un Dockerfile para ejecutarlo en un contenedor. Para construir y ejecutar la imagen:

1. **Construir la imagen:**

    ```bash
    docker build -t imdb-sentiment-api .
    ```

2. **Ejecutar el contenedor:**

    ```bash
    docker run -p 5000:5000 imdb-sentiment-api
    ```

La API estará disponible en `http://localhost:5000`.

## Estructura del Proyecto

```
imdb-sentiment-api/
├── app/
│   ├── controllers/           # Controladores de la API
│   ├── models/                # Modelos de TensorFlow y archivos del vectorizer
│   ├── routes/                # Rutas de la API
│   └── services/              # Servicios de negocio, como la predicción de sentimiento (No se suben a la repo por tamaño)
├── Dockerfile                 # Para contenerización con Docker
├── pyproject.toml             # Configuración del proyecto y dependencias
├── README.md                  # Este archivo
└── run.py                     # Punto de entrada de la aplicación
```

## Licencia

Este proyecto se distribuye bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.
