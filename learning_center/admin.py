from flask_admin import AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView


class UserView(ModelView):
    column_exclude_list = ['password']
    create_modal = True
    edit_modal = True


class DashboardView(AdminIndexView):

    @expose('/')
    def index(self):
        return self.render('admin_dashboard.html')
