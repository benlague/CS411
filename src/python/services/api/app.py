from .config import get_config
from .libs.auth import jwt, oauth, register_providers
from .libs.cache import cache
from .models import models  # noqa: F401
from .models.common.db import db
from .resources import (
    AuditAPI,
    HealthCheckAPI,
    LoginAPI,
    RegisterAPI,
    UserAPI,
    OAuthLoginAPI,
    OAuthAuthorizeAPI,
    YelpAPI,
    BestTimeAPI
)

from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate as DBMigrate
from flask_cors import CORS


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
jwt.init_app(app)

# Initialize oauth extention
oauth.init_app(app)
register_providers()

# Initialized redis cache extention
cache.init_app(app)

# Initialize Cors extention
CORS(app, supports_credentials=True)

# Attach API resources to routes
api.add_resource(AuditAPI, '/auditlog')
api.add_resource(HealthCheckAPI, '/healthcheck')
api.add_resource(LoginAPI, '/auth/login')
api.add_resource(RegisterAPI, '/auth/register')
api.add_resource(UserAPI, "/auth/user")
api.add_resource(OAuthLoginAPI, '/auth/oauth/login')
api.add_resource(OAuthAuthorizeAPI, '/auth/oauth/authorize')
api.add_resource(YelpAPI, '/yelp')
api.add_resource(BestTimeAPI, '/besttime')
