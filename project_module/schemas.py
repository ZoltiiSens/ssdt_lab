from marshmallow import Schema, fields


class UserSchema(Schema):
    name = fields.Str(required=True)


class CategorySchema(Schema):
    name = fields.Str(required=True)


class RecordSchema(Schema):
    sum = fields.Int(required=True)
    creation_date = fields.DateTime()
    user_id = fields.Int(required=True)
    category_id = fields.Int(required=True)


class RecordQuerySchema(Schema):
    user_id = fields.Str()
    category_id = fields.Str()


class AccountSchema(Schema):
    user_id = fields.Int(required=True)
    sum = fields.Int(required=True)
