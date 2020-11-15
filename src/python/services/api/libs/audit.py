from typing import Optional

from ..libs.respository import SQLAlchemyRepository
from ..models.models import AuditEntry

from flask import request


class AuditLog:
    instance: Optional["AuditLog"] = None

    def __init__(self, audit_entry_repo: SQLAlchemyRepository):
        self.audit_entry_repo = audit_entry_repo

    def _log_event(self, actor: str, activity: str, target: str = None):
        entry = AuditEntry(
            actor=actor,
            ip=request.remote_addr,
            activity=activity,
            target=target
        )
        self.audit_entry_repo.save(entry, commit=True)

    @classmethod
    def log_event(cls, actor: str, activity: str, target: str = None):
        assert AuditLog.instance is not None
        AuditLog.instance._log_event(actor, activity, target)
