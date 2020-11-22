from .config import get_config
from .libs.auth import login_manager, oath, on_user_login
from .models import models  # noqa: F401
from .models.common.db import db
from .resources import (
    AuditAPI,
    HealthCheckAPI,
    LoginAPI,
    RegisterAPI,
    LogoutAPI,
    UserAPI
)

from flask import Flask
from flask_login.signals import user_logged_in
from flask_restful import Api
from flask_migrate import Migrate as DBMigrate


# Initialize flask application
app = Flask(__name__)

# Configure flask application
app.config.from_object(get_config())

# Initialize flask integrations
api = Api(app, prefix='/api')
db.init_app(app)
db_migrate = DBMigrate(app, db)
login_manager.init_app(app)
oath.init_app(app)

# Register signal subscribers
user_logged_in.connect(on_user_login, app)

# Attach API resources to routes
api.add_resource(AuditAPI, '/auditlog')
api.add_resource(HealthCheckAPI, '/healthcheck')
api.add_resource(LoginAPI, '/auth/login')
api.add_resource(RegisterAPI, '/auth/register')
api.add_resource(LogoutAPI, '/auth/logout')
api.add_resource(UserAPI, "/auth/user")
