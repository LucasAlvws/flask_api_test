from marshmallow import fields, validate, ValidationError, validates_schema

from extensions import ma
from models.users import User

class UserSerializer(ma.SQLAlchemyAutoSchema):
    name = fields.String(required=True, validate=[validate.Length(min=3)])
    email = fields.String(required=True, validate=[validate.Email()])

    @validates_schema
    def validate_email(self, data, **kwargs):
        email = data.get('email')
        if User.query.filter_by(email=email).count():
            raise ValidationError(f"The {email} already exists.")

    class Meta:
        model = User
        load_instance = True
        exclude = ['id']