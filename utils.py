import os
from plugins.shared_orch.app_objects import db, ma


def configure_db_settings(app):
    db_user = os.environ.get("POSTGRES_USER", 'carrier')
    db_password = os.environ.get("POSTGRES_PASSWORD", 'password')
    db_name = os.environ.get("POSTGRES_DB", 'carrier')
    db_host = os.environ.get("POSTGRES_HOST", "127.0.0.1")
    db_port = os.environ.get("POSTGRES_PORT", 5432)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'


def init_app_objects(app):
    configure_db_settings(app)
    db.init_app(app)
    ma.init_app(app)