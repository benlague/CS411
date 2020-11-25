from flask.helpers import make_response
from .common.base import BaseResource
from ..libs.audit import log_event
from ..libs.auth import oauth
from ..libs.respository import create_repo
from ..models.models import User
from ..schemas.auth import (
    LoginSchema,
    RegisterSchema,
    UserSchema,
    UserUpdateSchema
)

from flask import request, jsonify
from flask_restful import abort, url_for
from flask_login import login_user, logout_user, login_required, current_user


class LoginAPI(BaseResource):
    def __init__(self):
        self.user_repo = create_repo(User)

    def post(self):
        params = self.validate_request(schema=LoginSchema, kwargs=request.json)  # noqa: E501
        email = params.get('email')
        password = params.get('password')
        remember_me = params.get('remember_me')

        users = self.user_repo.find_by({'email': email})

        if not users:
            abort(401, message=f'User with email {email} does not exist')

        user = users[0]
        if user.check_password(password=password):
            login_user(user, remember=remember_me)
        else:
            abort(401, message=f'Incorrect password for user with email {email}')  # noqa: E501

        log_event(actor=email, activity='login', target='account')

        return 200


class RegisterAPI(BaseResource):
    def __init__(self):
        self.user_repo = create_repo(User)

    def post(self):
        params = self.validate_request(schema=RegisterSchema, kwargs=request.json)  # noqa: E501
        email = params.get('email')
        password = params.get('password')
        first_name = params.get('first_name')
        last_name = params.get('last_name')

        users = self.user_repo.find_by({'email': email})

        if users:
            abort(400, message=f'User with email {email} already exists')

        user = User(email=email, first_name=first_name, last_name=last_name)
        user.set_password(password=password)

        self.user_repo.save(user, commit=True)

        log_event(actor=email, activity='register', target='account')

        return 201


class LogoutAPI(BaseResource):

    method_decorators = [login_required]

    def get(self):
        logout_user()


class UserAPI(BaseResource):

    method_decorators = [login_required]

    def __init__(self):
        self.user_repo = create_repo(User)

    def get(self):
        user_data = UserSchema().dump(current_user)
        return make_response(jsonify(user_data), 200)

    def post(self):
        params = self.validate_request(schema=UserUpdateSchema, kwargs=request.json)  # noqa: E501
        first_name = params.get('first_name')
        last_name = params.get('last_name')

        if first_name:
            current_user.first_name = first_name
        if last_name:
            current_user.last_name = last_name

        self.user_repo.save(current_user, commit=True)

        return 202

    def delete(self):
        self.user_repo.delete(current_user, commit=True)
        logout_user()

        return 204


class GithubOAuthLoginAPI(BaseResource):

    def get(self):
        authorize_endpoint = url_for('githuboauthauthorizeapi', _external=True)
        return oauth.github.authorize_redirect(authorize_endpoint)


class GithubOAuthAuthorizeAPI(BaseResource):
    def __init__(self):
        self.user_repo = create_repo(User)

    def get(self):
        oauth.github.authorize_access_token()

        # Get github user first and last name
        profile = oauth.github.get('user').json()
        first_name, last_name = profile['name'].split()

        # Get unique github user id
        user_id = profile['id']

        # Get github user primary email
        emails = oauth.github.get('user/emails').json()
        email = self.find_primary_email(emails=emails)

        # Create user in database if doesnt exist
        user = self.user_repo.get(user_id)
        if user is None:
            user = User(
                id=user_id,
                email=email,
                first_name=first_name,
                last_name=last_name
            )
            self.user_repo.save(user, commit=True)

        login_user(user)

    @staticmethod
    def find_primary_email(emails):
        for user_email in emails:
            if user_email['primary'] == "True":
                return user_email['email']
