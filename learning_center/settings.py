import os
from pathlib import Path

BASEDIR = Path(__file__).resolve().parent.parent


class Config():
    SECRET_KEY = os.getenv('SECRET_KEY', 'some extra secret string')

    SQLALCHEMY_DATABASE_URI = 'sqlite:///{database}'.format(
        database=BASEDIR.joinpath('data.sqlite'),
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
