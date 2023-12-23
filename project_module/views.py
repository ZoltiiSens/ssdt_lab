from flask import jsonify, request
# from flask_smorest import abort
from datetime import date
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
from project_module import app, db
from project_module.schemas import UserSchema, RecordSchema, AccountSchema, CategorySchema
from project_module.models import UserModel, RecordModel, AccountModel, CategoryModel

with app.app_context():
    db.create_all()
    db.create_all()
    db.session.commit()


# Work with User
@app.get("/user/<user_id>")
def get_user(user_id):
    user = UserModel.query.get_or_404(user_id)
    return {"id": user.id, "name": user.name}


@app.delete("/user/<user_id>")
def delete_user(user_id):
    user = UserModel.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return {"message": f"Success! User {user_id} deleted"}


@app.post("/user")
def create_user():
    newUserData = request.get_json()
    user_validation = UserSchema()
    try:
        user_validation.load(newUserData)
    except ValidationError as err:
        return jsonify({'error': err.messages}), 400
    user = UserModel(name=newUserData["name"])
    try:
        db.session.add(user)
        db.session.commit()
    except IntegrityError:
        return "There is en error in inputted data", 400
        # abort(
        #     400,
        #     message="There is en error in inputted data"
        # )
    user_dict = {"id": user.id, "name": user.name}
    return jsonify(user_dict), 200


@app.get("/users")
def get_users():
    return list({"id": user.id, "name": user.name} for user in UserModel.query.all())


# Work with category
@app.get("/category")
def get_category():
    category_id = request.args.get("id")
    category = UserModel.query.get_or_404(category_id)
    return {"id": category.id, "name": category.name}


@app.post("/category")
def create_category():
    newCategoryData = request.args
    category_validation = CategorySchema()
    try:
        category_validation.load(newCategoryData)
    except ValidationError as err:
        return jsonify({'error': err.messages}), 400
    category = CategoryModel(name=newCategoryData["name"])
    try:
        db.session.add(category)
        db.session.commit()
    except IntegrityError:
        return "There is en error in inputted data", 400
        # abort(
        #     400,
        #     message="There is en error in inputted data"
        # )
    return jsonify({"id": category.id, "name": category.name}), 200


@app.delete("/category")
def delete_category():
    category_id = request.args.get("id")
    category = CategoryModel.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return {"message": f"Success! Category {category_id} deleted"}


@app.get("/categories")
def get_categories():
    return list({"id": category.id, "name": category.name} for category in CategoryModel.query.all())


# Work with records
@app.get("/record/<record_id>")
def get_record(record_id):
    record = RecordModel.query.get_or_404(record_id)
    response = {
        "id": record.id,
        "sum": record.sum,
        "creation_date": record.creation_date,
        "user_id": record.user_id,
        "category_id": record.category_id
    }
    return response, 200


@app.delete("/record/<record_id>")
def delete_record(record_id):
    record = RecordModel.query.get_or_404(record_id)
    db.session.delete(record)
    db.session.commit()
    return {"message": f"Success! Record {record_id} deleted"}


@app.post("/record")
def create_record():
    newRecordData = request.args
    record_validation = RecordSchema()
    try:
        record_validation.load(newRecordData)
    except ValidationError as err:
        return jsonify({'error': err.messages}), 400
    user_account = AccountModel.query.filter_by(user_id=newRecordData["user_id"]).first()
    if not user_account:
        return "User have no account", 400
    record = RecordModel(sum=newRecordData["sum"], user_id=newRecordData["user_id"], category_id=newRecordData["category_id"])
    try:
        user_account.sum = float(user_account.sum) - float(record.sum)
        db.session.add(record)
        db.session.commit()
    except IntegrityError:
        return "There is en error in inputted data", 400
        # abort(
        #     400,
        #     message="There is en error in inputted data"
        # )
    response = {
        "id": record.id,
        "sum": record.sum,
        "creation_date": record.creation_date,
        "user_id": record.user_id,
        "category_id": record.category_id
    }
    return response, 200


@app.get("/record")
def get_filtered_records():
    categoryId = request.args.get('category_id')
    userId = request.args.get('user_id')
    records = []
    if not categoryId and not userId:
        return "pass at least one argument: category_id, user_id", 400
        # return abort(
        #     400,
        #     message="pass at least one argument: category_id, user_id"
        # )
    if not userId:
        records = RecordModel.query.filter_by(category_id=categoryId)
    if not categoryId:
        records = RecordModel.query.filter_by(user_id=userId)
    if categoryId and userId:
        records = RecordModel.query.filter_by(category_id=categoryId, user_id=userId)
    return list({"id": record.id, "sum": record.sum, "creation_date": record.creation_date, "user_id": record.user_id, "category_id": record.category_id} for record in records), 200


# Work with accounts
@app.post("/account")
def create_account():
    newAccountData = request.args
    account_validation = AccountSchema()
    try:
        account_validation.load(newAccountData)
    except ValidationError as err:
        return jsonify({'error': err.messages}), 400
    account = AccountModel(sum=newAccountData["sum"], user_id=newAccountData["user_id"])
    try:
        db.session.add(account)
        db.session.commit()
    except IntegrityError:
        return "There is en error in inputted data", 400
        # abort(
        #     400,
        #     message="There is en error in inputted data"
        # )
    return jsonify({"id": account.id, "sum": account.sum, "user_id": account.user_id}), 200


@app.get("/account/<account_id>")
def get_account(account_id):
    account = AccountModel.query.get_or_404(account_id)
    response = {
        "id": account.id,
        "sum": account.sum,
        "user_id": account.user_id
    }
    return response, 200


@app.put("/account/<account_id>")
def put_account(account_id):
    account = AccountModel.query.get_or_404(account_id)
    sum = request.args["sum"]
    account.sum += float(sum)
    db.session.commit()
    response = {
        "id": account.id,
        "sum": account.sum,
        "user_id": account.user_id
    }
    return response, 200


@app.get("/accounts")
def get_accounts():
    return list({"id": account.id, "sum": account.sum, "user_id": account.user_id} for account in AccountModel.query.all())


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
