from flask import Flask, jsonify
from datetime import date


app = Flask(__name__)


@app.route("/healthcheck")
def healthCheck():
    response = {
        'time': date.today(),
        'status': 200,
    }
    return jsonify(response), 200
