import time
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api")
def api():
    return jsonify(message="Hello World from the API!")

@app.route("/load")
def load():
    # Artificial CPU load for ~2 seconds
    end = time.time() + 2.0
    while time.time() < end:
        _ = sum(i * i for i in range(10000))
    return "Load test done"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
