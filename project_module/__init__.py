from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import project_module.views

app = Flask(__name__)
db = SQLAlchemy(app)

app.config.from_pyfile('config.py', silent=True)

