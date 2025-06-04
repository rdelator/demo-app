from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api")
def api():
    return jsonify(message="Hello World from the API!")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
