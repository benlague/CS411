from datetime import datetime

from .respository import create_repo
from ..models.models import User

from authlib.integrations.flask_client import OAuth
from flask_login import LoginManager, current_user


login_manager = LoginManager()
oauth = OAuth()

user_repo = create_repo(User)


def register_providers():
    oauth.register(
        name='github',
        access_token_url='https://github.com/login/oauth/access_token',
        authorize_url='https://github.com/login/oauth/authorize',
        api_base_url='https://api.github.com/',
        client_kwargs={'scope': 'read:user user:email'},
    )


@login_manager.user_loader
def user_loader(user_id):
    user = user_repo.get(user_id)
    return user or None


def on_user_login(app, **kwargs):
    current_user.last_login = datetime.now()
    user_repo.save(current_user, commit=True)
