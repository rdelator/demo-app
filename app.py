from flask import Flask, jsonify, render_template
import time
import threading

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api")
def api():
    return jsonify(message="Hello World from the API!")

@app.route("/load")
def load():
    # Run CPU-bound task in a blocking way for 5 seconds
    def cpu_stress():
        end_time = time.time() + 5
        while time.time() < end_time:
            _ = sum(i*i for i in range(10000))  # Simple heavy loop

    threads = []
    for _ in range(4):  # Adjust this number based on vCPU count
        t = threading.Thread(target=cpu_stress)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    return jsonify(message="CPU stress generated")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
