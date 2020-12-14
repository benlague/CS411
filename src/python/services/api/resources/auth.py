from flask.helpers import make_response
from .common.base import BaseResource
from ..libs.audit import log_event
from ..libs.auth import (
    oauth,
    login_required,
    get_current_user,
    create_jwt_access_token
)
from ..libs.respository import create_repo
from ..models.models import User
from ..schemas.auth import (
    LoginSchema,
    RegisterSchema,
    UserSchema,
    UserUpdateSchema
)

from flask import request, jsonify, redirect, current_app
from flask_restful import abort, url_for

from urllib.parse import urlencode


class LoginAPI(BaseResource):
    def __init__(self):
        self.user_repo = create_repo(User)

    def post(self):
        params = self.validate_request(schema=LoginSchema, kwargs=request.form)  # noqa: E501
        email = params.get('email')
        password = params.get('password')

        users = self.user_repo.find_by({'email': email})

        if not users:
            abort(401, message=f'User with email {email} does not exist')

        user = users[0]
        if not user.check_password(password=password):
            abort(401, message=f'Incorrect password for user with email {email}')  # noqa: E501

        log_event(actor=email, activity='login', target='account')

        resp = {
            'access_token': create_jwt_access_token(user=user),
            'user': UserSchema().dump(user)
        }

        return resp, 200


class RegisterAPI(BaseResource):
    def __init__(self):
        self.user_repo = create_repo(User)

    def post(self):
        params = self.validate_request(schema=RegisterSchema, kwargs=request.form)  # noqa: E501
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


class UserAPI(BaseResource):

    method_decorators = [login_required]

    def __init__(self):
        self.user_repo = create_repo(User)

    def get(self):
        user_data = UserSchema().dump(get_current_user())
        return make_response(jsonify(user_data), 200)

    def post(self):
        params = self.validate_request(schema=UserUpdateSchema, kwargs=request.form)  # noqa: E501
        first_name = params.get('first_name')
        last_name = params.get('last_name')

        current_user = get_current_user()

        if first_name:
            current_user.first_name = first_name
        if last_name:
            current_user.last_name = last_name

        self.user_repo.save(current_user, commit=True)

        return 202

    def delete(self):
        current_user = get_current_user()
        self.user_repo.delete(current_user, commit=True)
        return 204


class OAuthLoginAPI(BaseResource):

    def get(self):
        authorize_endpoint = url_for('oauthauthorizeapi', _external=True)
        return oauth.auth0.authorize_redirect(authorize_endpoint)


class OAuthAuthorizeAPI(BaseResource):
    def __init__(self):
        self.user_repo = create_repo(User)

    def get(self):
        oauth.auth0.authorize_access_token()

        resp = oauth.auth0.get('userinfo')
        userinfo = resp.json()

        first_name, last_name = userinfo['name'].split()
        email = userinfo['email']

        # Create user in database if doesnt exist
        users = self.user_repo.find_by(prop_dict={'email': email})
        if len(users) == 0:
            user = User(
                email=email,
                first_name=first_name,
                last_name=last_name
            )
            self.user_repo.save(user, commit=True)
        else:
            user = users[0]

        log_event(actor=email, activity='oauth login', target='account')

        return_to = f"{current_app.config['FRONTEND_URL']}/oauth?{urlencode({'access_token': create_jwt_access_token(user=user)})}"  # noqa: E501
        return redirect(return_to)
