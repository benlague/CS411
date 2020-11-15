from .config import get_config
from .libs.audit import AuditLog
from .libs.respository import SQLAlchemyRepository
from .models import models
from .models.common.db import db
from .resources import HealthCheckAPI, AuditAPI

from flask import Flask
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

# Initialize database repositories (tables)
audit_entry_repo = SQLAlchemyRepository(db=db, cls=models.AuditEntry)

# Misc setup
audit_log = AuditLog(audit_entry_repo)
AuditLog.instance = audit_log

# Attach API resources to routes
api.add_resource(AuditAPI, '/auditlog', resource_class_kwargs={'audit_entry_repo': audit_entry_repo})  # noqa: E501
api.add_resource(HealthCheckAPI, '/healthcheck')
