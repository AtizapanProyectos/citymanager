# Imagen base estable
FROM python:3.12-slim

# Variables de entorno para Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Instalamos dependencias para MySQL y limpieza de temporales
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Carpeta de la app
WORKDIR /app

# Instalación de librerías
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos todo el código
COPY . .

# Recolectamos estáticos (CSS, JS, imágenes del mapa)
RUN python manage.py collectstatic --noinput

# Puerto que usa Gunicorn
EXPOSE 8000

# Arrancamos con Gunicorn (asegúrate que city_manager sea el nombre de tu carpeta de settings)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "city_manager.wsgi:application", "--workers", "3"]