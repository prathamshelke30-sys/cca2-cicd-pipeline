FROM python:3.12-slim

WORKDIR /app

COPY app.py .
COPY requirements.txt .

EXPOSE 3000

CMD ["python", "-u", "app.py"]
