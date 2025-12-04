from flask import Flask, render_template
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

# ✅ THIS LINE IS MANDATORY
metrics = PrometheusMetrics(app)

@app.route("/")
def dashboard():
    return render_template("index.html")

# ✅ EXPLICIT FLASK METRIC (OPTIONAL BUT GOOD)
@app.route("/hello")
def hello():
    return "Hello from Flask + Prometheus!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

