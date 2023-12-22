import uuid

from flask import jsonify, request
from datetime import date
from project_module import app

users = {}
categories = {}
records = {}


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
    newUser = {
        "id": newUserId,
        **newUserData
    }
    users[newUserId] = newUser
    return newUser, 200


@app.get("/users")
def get_users():
    return jsonify(list(users.values())), 200


@app.get("/category")
def get_category():
    category_id = request.args.get("id")
    if category_id in categories.keys():
        return categories[category_id], 200
    else:
        return jsonify({}), 400


@app.post("/category")
def create_category():
    newCategoryName = request.args.get("name")
    newCategoryId = uuid.uuid4().hex
    newCategory = {
        "id": newCategoryId,
        "name": newCategoryName,
    }
    categories[newCategoryId] = newCategory
    return jsonify(newCategory), 200


@app.delete("/category")
def delete_category():
    category_id = request.args.get("id")
    if category_id in categories.keys():
        category = categories[category_id]
        del categories[category_id]
        return jsonify(category), 200
    else:
        return jsonify({}), 400


@app.get("/categories")
def get_categories():
    return jsonify(list(categories.values())), 200


@app.get("/record/<record_id>")
def get_record(record_id):
    if record_id in records.keys():
        return records[record_id], 200
    else:
        return jsonify({}), 400


@app.delete("/record/<record_id>")
def delete_record(record_id):
    if record_id in records.keys():
        record = records[record_id]
        del records[record_id]
        return jsonify(record), 200
    else:
        return jsonify({}), 400


@app.post("/record")
def create_record():
    newRecordId = uuid.uuid4().hex
    newRecord = {
        "id": newRecordId,
        "creation_date": date.today(),
        "sum": request.args.get("sum"),
        "user_id": request.args.get("user_id"),
        "category_id": request.args.get("category_id")
    }
    records[newRecordId] = newRecord
    return jsonify(newRecord), 200


@app.get("/record")
def get_filtered_records():
    categoryId = request.args.get('category_id')
    userId = request.args.get('user_id')
    result = []
    if not categoryId and not userId:
        return jsonify({"message": "pass at least one argument: category_id, user_id"}), 400
    if not userId:
        for record in records.values():
            if record["category_id"] == categoryId:
                result.append(record)
    elif not categoryId:
        for record in records.values():
            if record["user_id"] == userId:
                result.append(record)
    else:
        for record in records.values():
            if record["user_id"] == userId and record["category_id"] == categoryId:
                result.append(record)
    return jsonify(result), 200


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
