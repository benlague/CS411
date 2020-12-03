from .common.base import BaseSchema
from ..models.models import User

from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class LoginSchema(BaseSchema):
    """ /api/auth/login - POST

    Parameters:
     - email (str)
     - password (str)
    """
    email = fields.Str(required=True)
    password = fields.Str(required=True)


class RegisterSchema(BaseSchema):
    """ /api/auth/register - POST

    Parameters:
     - email (str)
     - password (str)
     - first_name (str)
     - last_name (str)
    """
    email = fields.Email(required=True)
    password = fields.Str(required=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)


class UserSchema(SQLAlchemyAutoSchema):
    """ /api/auth/user - GET

    Returns:
     - email (str)
     - first_name (str)
     - last_name (str)
     - last_login (str)
    """
    class Meta:
        model = User
        exclude = ("password", "id")


class UserUpdateSchema(BaseSchema):
    """ /api/auth/user - POST

    Returns:
     - first_name (str)
     - last_name (str)
    """
    first_name = fields.Str(required=False)
    last_name = fields.Str(required=False)
