FROM python:3.12-slim

WORKDIR /app

COPY counter_app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY counter_app/ .

EXPOSE 8000

CMD ["python", "server.py"]
