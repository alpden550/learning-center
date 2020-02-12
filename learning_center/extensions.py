from flask_admin import Admin
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from learning_center.admin import DashboardView

admin = Admin(index_view=DashboardView(url='/'), name='Stepic CRM')
db = SQLAlchemy()
migrate = Migrate()
