from flask_login import UserMixin
from sqlalchemy import event
from sqlalchemy.exc import IntegrityError
from sqlalchemy_utils import ChoiceType, EmailType, PhoneNumber
from werkzeug.security import check_password_hash, generate_password_hash

from learning_center.extensions import db, login


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


class User(UserMixin, CRUDMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(EmailType, unique=True, index=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<User {self.uid} – {self.username}>'


class Group(CRUDMixin, db.Model):
    STATUS_TYPES = [
        ('RECRUITING', 'Набирается'),
        ('RECRUITED', 'Набрана'),
        ('GOING', 'Идет'),
        ('ARCHIVE', 'В архиве'),
    ]
    COURSE_TYPES = [
        ('PYTHON', 'Python'),
        ('flask', 'Flask'),
        ('VUE', 'Vue'),
        ('DJANGO', 'Django'),
        ('PHP', 'PHP'),
        ('HTML', 'HTML'),
    ]
    uid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False, unique=True)
    status = db.Column(ChoiceType(STATUS_TYPES), nullable=False, default='RECRUITING')
    course = db.Column(ChoiceType(COURSE_TYPES), nullable=False, default='PYTHON')
    started_at = db.Column(db.Date)
    applicants = db.relationship('Applicant', back_populates='group')
    max_applicants = db.Column(
        db.Enum('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15'),
        nullable=False,
        default='10',
    )

    @property
    def numbers_of_applicants(self):
        return len(self.applicants)

    def __repr__(self):
        return f'<Group {self.uid} – {self.title}>'


class Applicant(CRUDMixin, db.Model):
    STATUS_TYPES = [
        ('NEW', 'Новая'),
        ('PROCESSED', 'В процессе'),
        ('PAID', 'Оплачена'),
        ('DISTRIBUTED', 'Распределена в группу'),
    ]
    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String)
    email = db.Column(EmailType, unique=True, index=True, nullable=False)
    status = db.Column(ChoiceType(STATUS_TYPES), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('group.uid'))
    group = db.relationship('Group', back_populates='applicants')

    def __repr__(self):
        return f'<Applicant {self.uid} – {self.name}>'


@event.listens_for(User.password, 'set', retval=True)
def hash_user_password(target, value, *args):  # noqa:WPS110
    return generate_password_hash(value)


@event.listens_for(Applicant.phone, 'set', retval=True)
def format_phone(turget, number, *args):
    return PhoneNumber(number, region='RU').international


@login.user_loader
def load_user(uid):
    return User.query.get(int(uid))
