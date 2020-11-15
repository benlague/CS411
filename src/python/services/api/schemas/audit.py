from datetime import datetime

from .common.base import BaseSchema
from ..models.models import AuditEntry

from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field


class AuditGetSchema(BaseSchema):
    size = fields.Int(required=False)
    start = fields.DateTime(r"%m/%d/%Y %I:%M %p", required=False)


class AuditEntrySchema(SQLAlchemySchema):
    class Meta:
        model = AuditEntry
        load_instance = False

    actor = auto_field()
    ip = auto_field()
    activity = auto_field()
    target = auto_field()
    timestamp = fields.Method("get_timestamp", type="integer")

    def get_timestamp(self, audit_entry):
        return datetime.timestamp(audit_entry.created_at)
