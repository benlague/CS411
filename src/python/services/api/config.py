import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    DEBUG = True
    # Uncomment this line if youd like to use sqlite instead of postgres
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')  # noqa: E501
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:123@postgres:5432/test"  # noqa: E501


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    # Uncomment this line if youd like to use sqlite instead of postgres
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')  # noqa: E501
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')  # noqa: E501


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')  # noqa: E501


config_by_environment = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)


def get_config():
    environment = os.environ['ENVIRONMENT']
    return config_by_environment[environment]
