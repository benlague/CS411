from .common.db import db
from .common.mixins import AuditMixin


class AuditEntry(db.Model, AuditMixin):
    __tablename__ = "audit_entry"
    id = db.Column(db.Integer, primary_key=True)
    actor = db.Column(db.Text, nullable=False)
    ip = db.Column(db.Text)
    activity = db.Column(db.Text, nullable=False)
    target = db.Column(db.Text)
