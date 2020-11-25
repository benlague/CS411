from .config import get_config
from .libs.auth import login_manager, oauth, on_user_login, register_providers
from .models import models  # noqa: F401
from .models.common.db import db
from .resources import (
    AuditAPI,
    HealthCheckAPI,
    LoginAPI,
    RegisterAPI,
    LogoutAPI,
    UserAPI,
    GithubOAuthLoginAPI,
    GithubOAuthAuthorizeAPI
)

from flask import Flask
from flask_login.signals import user_logged_in
from flask_restful import Api
from flask_migrate import Migrate as DBMigrate


# Initialize flask application
app = Flask(__name__)

# Configure flask application
app.config.from_object(get_config())

# Initialize flask api
api = Api(app, prefix='/api')

# Initialize sqlalchemy extention
db.init_app(app)

# Initialize alembic extention
db_migrate = DBMigrate(app, db)

# Initalize login manager extention
login_manager.init_app(app)

# Initialize oauth extention
oauth.init_app(app)
register_providers()

# Register signal subscribers
user_logged_in.connect(on_user_login, app)

# Attach API resources to routes
api.add_resource(AuditAPI, '/auditlog')
api.add_resource(HealthCheckAPI, '/healthcheck')
api.add_resource(LoginAPI, '/auth/login')
api.add_resource(RegisterAPI, '/auth/register')
api.add_resource(LogoutAPI, '/auth/logout')
api.add_resource(UserAPI, "/auth/user")
api.add_resource(GithubOAuthLoginAPI, '/auth/oauth/github')
api.add_resource(GithubOAuthAuthorizeAPI, '/auth/oauth/github/authorize')
