# Usar la imagen oficial de Python 3.11 slim como imagen base
FROM python:3.11-slim

# Establecer variables de entorno para evitar buffering y forzar UTF-8
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUTF8=1

# Establecer el directorio de trabajo de la aplicación
WORKDIR /app

# Actualizar el sistema e instalar dependencias del sistema necesarias para compilación (opcional)
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential && \
    rm -rf /var/lib/apt/lists/*

# Copiar el archivo de configuración del proyecto (pyproject.toml)
COPY pyproject.toml ./

# Copiar el resto del código fuente a la imagen
COPY . .

# Actualizar pip e instalar las dependencias requeridas
RUN pip install --upgrade pip && \
    pip install flask flask-cors python-dotenv waitress tensorflow

# Exponer el puerto donde se ejecutará la aplicación (por defecto, Flask usa 5000)
EXPOSE 5000

# Establecer variables de entorno para Flask
ENV FLASK_APP=run.py
ENV FLASK_ENV=production

# Comando de inicio utilizando waitress para servir la aplicación
CMD ["waitress-serve", "--listen=0.0.0.0:5000", "run:app"]