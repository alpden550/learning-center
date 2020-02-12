from sqlalchemy.exc import IntegrityError
from sqlalchemy_utils import EmailType, PhoneNumberType
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
    email = db.Column(EmailType, unique=True, index=True, nullable=False)
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
    applicants = db.relationship('Applicant', back_populates='group', lazy='joined')

    def __repr__(self):
        return f'<Group {self.uid} – {self.title}>'


class Applicant(CRUDMixin, db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    phone = db.Column(PhoneNumberType(region='RU'))
    email = db.Column(EmailType, unique=True, index=True, nullable=False)
    status = db.Column(
        db.Enum('NEW', 'PROCESSED', 'PAID', 'DISTRIBUTED', name='applicant_status'), nullable=False,
    )
    group_id = db.Column(db.Integer, db.ForeignKey('group.uid'), nullable=False)
    group = db.relationship('Group', back_populates='applicants')

    def __repr__(self):
        return f'<Applicant {self.uid} – {self.name}>'
