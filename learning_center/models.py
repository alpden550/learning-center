from sqlalchemy.exc import IntegrityError
from werkzeug.security import check_password_hash, generate_password_hash

from learning_center.extensions import db


class CRUDMixin:
    def save(self):
        db.session.add(self)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class User(CRUDMixin, db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(254), unique=True, index=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.uid} – {self.name}>'


class Group(CRUDMixin, db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False, unique=True)
    status = db.Column(
        db.Enum('RECRUITING', 'RECRUITED', 'GOING', 'ARCHIVE', name='group_status'), nullable=False,
    )
    course = db.Column(
        db.Enum('PYTHON', 'VUE', 'DJANGO', 'PHP', 'HTML', name='group_course'), nullable=False,
    )
    started_at = db.Column(db.Date)

    def __repr__(self):
        return f'<Group {self.uid} – {self.title}>'
