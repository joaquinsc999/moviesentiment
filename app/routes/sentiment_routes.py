from flask import Blueprint, request
from app.controllers.sentiment_controllers import binary_sentiment_prediction_controller
from app.utils import loggers
sentiment_routes = Blueprint("sentiment_routes", __name__)

@sentiment_routes.route("/binary-sentiment", methods=["POST"])
def binary_sentiment_prediction():
    data = request.json
    loggers.info(f"Predicción de sentimiento binario recibida en route {data}")
    return binary_sentiment_prediction_controller(data)
