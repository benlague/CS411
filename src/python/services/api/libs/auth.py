from .respository import create_repo
from ..models.models import User

from authlib.integrations.flask_client import OAuth
from flask_jwt_extended import (
    JWTManager,
    jwt_required,
    create_access_token,
    current_user
)


jwt = JWTManager()
oauth = OAuth()

user_repo = create_repo(User)


def register_providers():
    oauth.register(
        name='auth0',
        api_base_url='https://dev-8m4p1t3y.auth0.com',
        access_token_url='https://dev-8m4p1t3y.auth0.com/oauth/token',
        authorize_url='https://dev-8m4p1t3y.auth0.com/authorize',
        client_kwargs={
            'scope': 'openid profile email',
        }
    )


@jwt.user_loader_callback_loader
def user_loader(user_id):
    user = user_repo.get(user_id)
    return user or None


def create_jwt_access_token(user: User):
    return create_access_token(identity=user.id)


def get_current_user():
    return current_user


login_required = jwt_required
