import os
os.environ["PYTHONUTF8"] = "1"

import tensorflow as tf
import pickle

# Directorio actual del archivo
current_dir = os.path.dirname(os.path.abspath(__file__))

# Cargar el vectorizer: se supone que lo guardaste en 'vectorizer_config_3.pkl'
# que contiene una tupla (config, vocab)
vectorizer_config_path = os.path.join(current_dir, "..", "models", "vectorizer_config_3.pkl")
with open(vectorizer_config_path, "rb") as f:
    config, _, vocab = pickle.load(f)

# Reconstruir la capa TextVectorization a partir de su configuración
vectorizer = tf.keras.layers.TextVectorization.from_config(config)
# Establecemos el vocabulario, lo que construye internamente la lookup table
vectorizer.set_vocabulary(vocab)

# Cargar el modelo guardado en formato .keras
model_path = os.path.join(current_dir, "..", "models", "sentiment_model.keras")
model = tf.keras.models.load_model(model_path)

def get_binary_sentiment_prediction(text):
    # El vectorizer se encarga de convertir el texto en secuencia
    sequence = vectorizer(tf.constant([text]))
    prediction = model.predict(sequence)
    sentiment = "positive" if prediction[0][0] > 0.5 else "negative"
    confidence = float(prediction[0][0])
    
    return {
        "sentiment": sentiment,
        "confidence": confidence
    }
