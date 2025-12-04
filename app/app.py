from flask import Flask, render_template
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

# ✅ Prometheus metrics
metrics = PrometheusMetrics(app)

# This creates flask_http_requests_total automatically
metrics.info('app_info', 'Flask App Info', version='1.0.0')

@app.route('/')
def dashboard():
    return render_template("index.html")

@app.route('/health')
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

