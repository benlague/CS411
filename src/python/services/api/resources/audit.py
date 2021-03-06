from .common.base import BaseResource
from ..libs.respository import create_repo
from ..models.models import AuditEntry
from ..schemas.audit import AuditGetSchema, AuditEntrySchema

from flask import request, jsonify, make_response


class AuditAPI(BaseResource):
    def __init__(self):
        self.audit_entry_repo = create_repo(AuditEntry)

    def get(self):
        params = self.validate_request(schema=AuditGetSchema, kwargs=request.values)  # noqa: E501
        filters = []
        if "start" in params:
            filters.append((
                AuditEntry.created_at > params.get('start')
            ))
        audit_entries = self.audit_entry_repo.find_by(
            filters=filters,
            limit=params.get('size', None)
        )
        response = AuditEntrySchema().dump(audit_entries, many=True)
        return make_response(jsonify(response), 200)
