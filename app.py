from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "API OK 🚀"

@app.route("/api/teste")
def teste():
    return jsonify({"status": "ok"})
