FROM python:3.9-slim

WORKDIR /app

# Instalar dependencias necesarias (ffmpeg para manejo de audio)
RUN apt-get update && apt-get install -y ffmpeg && apt-get clean

# Instalar dependencias de Python
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente al contenedor
COPY . /app

# Crear un usuario no root para ejecutar la aplicación
RUN useradd -m appuser
RUN chown -R appuser:appuser /app

# Cambiar al usuario no root
USER appuser

# Exponer el puerto 5000 para Flask
EXPOSE 5000

# Agregar src al PYTHONPATH
ENV PYTHONPATH=/app

# Establecer la variable de entorno FLASK_APP para que apunte a la aplicación
ENV FLASK_APP=/app/adapters/flask_api_adapter.py

# Comando para ejecutar la aplicación Flask
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]
