from fastapi import FastAPI
from fastapi.responses import Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time
import random

app = FastAPI()

REQUEST_COUNT = Counter('weather_requests_total', 'Total requests', ['endpoint'])
REQUEST_LATENCY = Histogram('weather_request_latency_seconds', 'Request latency')

@app.get("/weather/{city}")
def get_weather(city: str):
    REQUEST_COUNT.labels(endpoint='/weather').inc()
    with REQUEST_LATENCY.time():
        time.sleep(random.uniform(0.05, 0.3))  # имитация похода во внешний API
        temp = random.randint(-10, 30)
    return {"city": city, "temperature": temp}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)# trigger ci
