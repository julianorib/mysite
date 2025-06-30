from flask import Flask, render_template
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route("/")
def inicial():
  return render_template("index.html")

@app.route("/blue")
def blue():
  return render_template("blue.html")

@app.route("/green")
def green():
  return render_template("green.html")

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=int("8080"))
