from app.services.sentiment_services import get_binary_sentiment_prediction
from app.utils import loggers
from app.utils.responses import json_response

def binary_sentiment_prediction_controller(data):
    loggers.info(f"Predicción de sentimiento binario recibida: {data}")
    return json_response(get_binary_sentiment_prediction(data["text"]))
