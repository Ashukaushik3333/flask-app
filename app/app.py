from flask import Flask, render_template
from prometheus_client import Counter, Histogram, generate_latest
import time

app = Flask(__name__)

REQUEST_COUNT = Counter(
    'flask_requests_total',
    'Total HTTP Requests',
    ['method', 'endpoint']
)

REQUEST_LATENCY = Histogram(
    'flask_request_latency_seconds',
    'Request latency'
)

@app.route('/')
def dashboard():
    REQUEST_COUNT.labels('GET', '/').inc()
    start = time.time()

    response = render_template("index.html")

    REQUEST_LATENCY.observe(time.time() - start)
    return response

@app.route('/metrics')
def metrics():
    return generate_latest(), 200

