import json
import tensorflow as tf
import numpy as np
import os

def init():
    global model
    # Ruta al archivo del modelo
    model_path = os.path.join(os.getenv('AZUREML_MODEL_DIR'), 'tf_sentiment_classifier')
    # Carga del modelo
    model = tf.keras.models.load_model(model_path)

def run(data):
    try:
        # Parsear los datos de entrada
        input_data = json.loads(data)
        # Convertir los datos a un arreglo de NumPy
        input_array = tf.constant(input_data['data'])
        # Realizar la predicción
        predictions = model.predict(input_array)
        # Devolver las predicciones como JSON
        return json.dumps({'predictions': predictions.tolist()})
    except Exception as e:
        error = str(e)
        return json.dumps({'error': error})
