# Dockerfile para Python
FROM python:3.9-slim
WORKDIR /app
COPY seriefibonacci.py .
CMD ["python", "seriefibonacci.py"]
