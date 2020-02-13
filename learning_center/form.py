from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField


class LoginForm(FlaskForm):
    username = StringField()
    password = PasswordField()
    is_remembered = BooleanField(label='Запомнить меня')
