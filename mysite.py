from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicial():
  return render_template("index.html")

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=int("8080"),debug=True)
