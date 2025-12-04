from flask import Flask, render_template
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# ✅ Prometheus Metrics
REQUEST_COUNT = Counter(
    "flask_http_requests_total",
    "Total HTTP Requests",
    ["method", "endpoint"]
)

@app.route("/")
def dashboard():
    REQUEST_COUNT.labels(method="GET", endpoint="/").inc()
    return render_template("index.html")

@app.route("/health")
def health():
    REQUEST_COUNT.labels(method="GET", endpoint="/health").inc()
    return {"status": "UP"}

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

