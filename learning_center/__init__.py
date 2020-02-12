import click
from flask import Flask
from flask_admin.contrib.sqla import ModelView

from learning_center.blueprints.bp_admin import admin_bp
from learning_center.extensions import admin, db, migrate
from learning_center.models import Applicant, Group, User
from learning_center.settings import Config


def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    register_extensions(app)
    register_commands(app)

    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Group, db.session))
    admin.add_view(ModelView(Applicant, db.session))

    return app


def register_extensions(app):
    db.init_app(app)
    admin.init_app(app)
    migrate.init_app(app, db)


def register_commands(app):

    @app.cli.command()
    def init():
        db.drop_all()
        db.create_all()
        click.echo('Initialized empy database.')
