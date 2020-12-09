import time

from .cache import cache as redis_db
from ..models.common.db import db as postgres_db

from sqlalchemy import text


class HealthCheck:
    def __init__(self, health_check, parameters={}, name=None):
        self.health_check: callable = health_check
        self.name = name or self.health_check.__name__
        self.parameters: dict = parameters

    def run(self):
        return self.health_check(**self.parameters)


def _postgres_available(**kwargs):
    postgres_db.engine.execute(text("SELECT 1"))


def _redis_available(**kwargs):
    test_key = f'TEST_{time.time()}'
    redis_db.set(test_key, 'test')
    redis_db.get(test_key)


health_checks = [
    HealthCheck(_postgres_available, name='Postgres available?'),
    HealthCheck(_redis_available, name='Redis available?')
]
