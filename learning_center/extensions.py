from flask_admin import Admin
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

from learning_center.admin import DashboardView

admin = Admin(index_view=DashboardView(url='/'), name='Stepic CRM')
csrf = CSRFProtect()
db = SQLAlchemy()
login = LoginManager()
migrate = Migrate()
