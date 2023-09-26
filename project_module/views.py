from flask import Flask

app = Flask(__name__)


@app.route("/healthcheck")
def healthСheck():
    return "<p>Health check page</p>"
