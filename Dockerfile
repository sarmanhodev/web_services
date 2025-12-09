FROM python:3.11-slim

WORKDIR /app

# Copia apenas requirements primeiro (melhor cache)
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Agora copia o resto do projeto
COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
