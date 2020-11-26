from typing import Optional

from ..libs.respository import create_repo
from ..models.models import AuditEntry

from flask import request


class AuditLog:
    instance: Optional["AuditLog"] = None

    def __init__(self):
        self.audit_entry_repo = create_repo(AuditEntry)

    def _log_event(self, actor: str, activity: str, target: str = None):
        entry = AuditEntry(
            actor=actor,
            ip=request.remote_addr,
            activity=activity,
            target=target
        )
        self.audit_entry_repo.save(entry, commit=True)


def log_event(actor: str, activity: str, target: str = None):
    if AuditLog.instance is None:
        audit_log = AuditLog()
        AuditLog.instance = audit_log
    AuditLog.instance._log_event(actor, activity, target)
