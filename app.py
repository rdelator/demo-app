import time
import threading
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
    def burn_cpu():
        end = time.time() + 10  # Increase duration for stress
        while time.time() < end:
            _ = sum(i * i for i in range(1000000))  # Heavy calculation

    threads = []
    for _ in range(4):  # Run 4 threads to stress multiple cores
        t = threading.Thread(target=burn_cpu)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    return "🔥 Maximum CPU load generated!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
