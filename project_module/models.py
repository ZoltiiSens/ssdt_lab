from project_module import db
from sqlalchemy.sql import func


class UserModel(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(256), unique=False, nullable=False)

    record = db.relationship("RecordModel", back_populates="user", lazy="dynamic")
    account = db.relationship("AccountModel", back_populates="user", lazy="dynamic")


class CategoryModel(db.Model):
    __tablename__ = "category"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)

    record = db.relationship("RecordModel", back_populates="category", lazy="dynamic")


class RecordModel(db.Model):
    __tablename__ = "record"
    id = db.Column(db.Integer, primary_key=True)
    sum = db.Column(db.Float, unique=False, nullable=False)
    creation_date = db.Column(db.TIMESTAMP, server_default=func.now())
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        unique=False,
        nullable=False
    )
    category_id = db.Column(
        db.Integer,
        db.ForeignKey("category.id"),
        unique=False,
        nullable=False
    )

    user = db.relationship("UserModel", back_populates="record")
    category = db.relationship("CategoryModel", back_populates="record")


class AccountModel(db.Model):
    __tablename__ = "account"

    id = db.Column(db.Integer, primary_key=True)
    sum = db.Column(db.Float, unique=False, nullable=False, default=0)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        unique=True,
        nullable=False
    )

    user = db.relationship("UserModel", back_populates="account", single_parent=True)
