# Imagen base
FROM python:3.11

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente
COPY ./app ./app

# Comando para ejecutar la app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
