import time
import threading
import os
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
    def burn():
        end = time.time() + 30  # Load duration in seconds
        while time.time() < end:
            x = 0
            for i in range(10**6):
                x += i ** 2  # Tight CPU-bound loop

    num_threads = os.cpu_count() or 4  # Use number of available CPU cores
    threads = []

    for _ in range(num_threads):
        t = threading.Thread(target=burn)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    return f"🔥 Heavy load generated on {num_threads} threads for 30s."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
