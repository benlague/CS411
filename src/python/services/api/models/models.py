from .common.db import db
from .common.mixins import AuditMixin

from werkzeug.security import generate_password_hash, check_password_hash


class AuditEntry(db.Model, AuditMixin):
    __tablename__ = "audit_entry"
    id = db.Column(db.Integer, primary_key=True)
    actor = db.Column(db.Text, nullable=False)
    ip = db.Column(db.Text)
    activity = db.Column(db.Text, nullable=False)
    target = db.Column(db.Text)


class User(db.Model, AuditMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(40), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=True)
    last_login = db.Column(db.DateTime, nullable=True)

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(
            password,
            method='sha256'
        )

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.email)
