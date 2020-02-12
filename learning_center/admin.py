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
    column_labels = {
        'title': 'Курс',
        'status': 'Статус курса',
        'course': 'Предмет',
        'started_at': 'Старт',
        'applicants': 'Участники',
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
        return self.render('admin_dashboard.html')
