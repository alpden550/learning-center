from flask_admin import AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView


class UserView(ModelView):
    column_exclude_list = ('password',)
    column_labels = {
        'username': 'Username',
        'email': 'Почта',
        'password': 'Пароль',
    }
    create_modal = True
    edit_modal = True


class GroupView(ModelView):
    column_list = (
        'title', 'status', 'course', 'started_at', 'max_applicants', 'numbers_of_applicants',
    )
    column_labels = {
        'title': 'Курс',
        'status': 'Статус курса',
        'course': 'Предмет',
        'started_at': 'Старт',
        'applicants': 'Участники',
        'max_applicants': 'Макс. человек',
        'numbers_of_applicants': 'Набрано',
    }


class ApplicantView(ModelView):
    column_labels = {
        'name': 'Имя',
        'phone': 'Телефон',
        'email': 'Почта',
        'status': 'Статус',
        'group': 'Группа',
    }


class DashboardView(AdminIndexView):

    @expose('/')
    def index(self):
        from learning_center.models import Group, Applicant  # noqa:WPS433
        groups = Group.query.all()
        appliciants = Applicant.query.all()
        distributed = len(appliciants)
        counted = [appliciant.status.code for appliciant in appliciants].count('NEW')
        return self.render(
            'admin_dashboard.html',
            groups=groups,
            new_groups=groups[:3],
            distributed=distributed,
            counted=counted,
        )
