from .common.base import BaseSchema
from ..models.models import User

from marshmallow import fields, validate
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class LoginSchema(BaseSchema):
    """ /api/auth/login - POST

    Parameters:
     - email (str)
     - password (str)
     - remember_me (bool)
    """
    email = fields.Str(required=True)
    password = fields.Str(required=True)
    remember_me = fields.Bool(
        truthy=['true'],
        falsy=['false'],
        required=False,
        default=False
    )


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


class OAuthLoginSchema(BaseSchema):
    """ /api/oauth/login - POST

    Parameters:
     - provider (str)
    """
    provider = fields.Str(
        required=True,
        validate=validate.OneOf(['facebook', 'twitter'])
    )


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
