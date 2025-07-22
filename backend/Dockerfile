# Folosim Python 3.11 slim ca bază
FROM python:3.11-slim

# Setăm variabila de mediu pentru a nu scrie bytecode și a avea ieșire bufferizată
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Setăm directorul de lucru în container
WORKDIR /app

# Instalăm dependențe de sistem necesare
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiem fișierul requirements
COPY backend/requirements.txt .

# Instalăm dependențele Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copiem tot codul backend (presupunem că docker-compose montează volumul)
COPY backend/ .

# Expunem portul pe care rulează FastAPI (uvicorn)
EXPOSE 8000

# Comanda default pentru a porni serverul API (poate fi suprascrisă în docker-compose)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
