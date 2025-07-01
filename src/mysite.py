import os
from flask import Flask, render_template
from prometheus_flask_exporter import PrometheusMetrics
import mysql.connector
from mysql.connector import Error

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

@app.route("/red")
def db():
    return render_template("red.html")

@app.route("/db")
def db_check():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST", ""),
            user=os.getenv("DB_USER", ""),
            password=os.getenv("DB_PASSWORD", ""),
            database=os.getenv("DB_NAME", "")
        )

        if connection.is_connected():
            return "Conexão com o banco de dados: OK"

    except Error as e:
        return f"Conexão com o banco de dados: Falha - {str(e)}"

    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("8080"))
