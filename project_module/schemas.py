from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    account_id = fields.Str(required=True)


class CategorySchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)


class RecordSchema(Schema):
    id = fields.Str(dump_only=True)
    user_id = fields.Str(required=True)
    category_id = fields.Str(required=True)
    currency_id = fields.Str(required=True)


class RecordQuerySchema(Schema):
    user_id = fields.Str()
    category_id = fields.Str()


class AccountSchema(Schema):
    user_id = fields.Str()
    summary = fields.Int()
