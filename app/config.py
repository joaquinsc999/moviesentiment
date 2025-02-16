import os
from dotenv import load_dotenv

# Cargar las variables definidas en el archivo .env
load_dotenv()

class Config:
    DEBUG = True
    PORT = os.getenv('PORT')
    AMBIENTE = os.getenv('AMBIENTE')
    AZURE_OPENAI_API_KEY = os.getenv('AZURE_OPENAI_API_KEY')
    AZURE_OPENAI_API_VERSION = os.getenv('AZURE_OPENAI_API_VERSION')
    AZURE_OPENAI_ENDPOINT = os.getenv('AZURE_OPENAI_ENDPOINT')

