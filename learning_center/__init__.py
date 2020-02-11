from flask import Flask

from learning_center.blueprints.admin import admin_bp
from learning_center.extensions import db, toolbar
from learning_center.settings import Config


def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    db.init_app(app)
    toolbar.init_app(app)


def register_blueprints(app):
    app.register_blueprint(admin_bp, url_prefix='/admin')
