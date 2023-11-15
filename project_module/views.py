import uuid

from flask import Flask, jsonify, request
from datetime import date


app = Flask(__name__)
users = {}
categories = {}
record = {}


@app.get("/user/<user_id>")
def get_user(user_id):
    if user_id in users.keys():
        return users[user_id], 200
    else:
        return jsonify({}), 400


@app.delete("/user/<user_id>")
def delete_user(user_id):
    if user_id in users.keys():
        user = users[user_id]
        del users[user_id]
        return jsonify(user), 200
    else:
        return jsonify({}), 400


@app.post("/user")
def create_user():
    newUserData = request.get_json()
    newUserId = uuid.uuid4().hex
    newUser = {"id": newUserId, **newUserData}
    users[newUserId] = newUser
    return jsonify(newUser), 200


@app.get("/users")
def get_users():
    return jsonify(list(users.values())), 200


@app.get("/category")
def get_category():
    return "getcategory", 200


@app.post("/category")
def create_category():
    return "createcategory", 200


@app.delete("/category")
def delete_category():
    return "deletecategory", 200


@app.get("/record/<int:record_id>")
def get_record(record_id):
    return f"getrecord {record_id}", 200


@app.delete("/record/<int:record_id>")
def delete_record(record_id):
    return f"deleterecord {record_id}", 200


@app.post("/record")
def create_record():
    return f"createrecord", 200


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
