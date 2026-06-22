FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install -e .

EXPOSE 8000

CMD ["sh", "-c", "uvicorn stock.api:app --host 0.0.0.0 --port ${PORT:-8000}"]