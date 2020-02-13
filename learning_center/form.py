from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField


class LoginForm(FlaskForm):
    username = StringField(label='')
    password = PasswordField(label='')
