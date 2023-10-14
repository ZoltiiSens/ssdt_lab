from flask import Flask, jsonify
from datetime import date


app = Flask(__name__)


@app.route("/")
def homepage():
    response = "<h1>Hi everyone!</h1>"
    return response, 200


@app.route("/healthcheck")
def healthCheck():
    response = {
        'time': date.today(),
        'status': 200,
    }
    return jsonify(response), 200
