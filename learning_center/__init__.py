import click
from flask import Flask, render_template, session

from learning_center.admin import ApplicantView, GroupView, UserView
from learning_center.extensions import admin, csrf, db, migrate, login
from learning_center.form import LoginForm
from learning_center.models import Applicant, Group, User
from learning_center.settings import Config


def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    register_extensions(app)
    register_commands(app)
    register_admins()

    return app


def register_extensions(app):
    db.init_app(app)
    admin.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)
    login.init_app(app)


def register_admins():
    admin.add_view(UserView(User, db.session, name='Пользователи'))
    admin.add_view(GroupView(Group, db.session, name='Группы'))
    admin.add_view(ApplicantView(Applicant, db.session, name='Заявки'))


def register_commands(app):

    @app.cli.command()
    def init():
        """Create empty database"""
        db.drop_all()
        db.create_all()
        click.echo('Initialized empyy database.')

    @app.cli.command()
    @click.option('-n', '--name', default='admin', help='Username for admin')
    @click.option('-e', '--email', default='admin@admin.com', help='Email for admin')
    @click.option('-p', '--password', default='1111', help='Password for admin')
    def admin(name, email, password):
        """Create empty database and default admin"""
        db.drop_all()
        click.echo('Initialized empty database.')
        db.create_all()
        admin = User(username=name, email=email, password=password)
        admin.save()
        click.echo('Default admin was created.')
