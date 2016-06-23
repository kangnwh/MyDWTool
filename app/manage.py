from flask import Flask
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
#from flask.ext.sqlalchemy import SQLAlchemy
from app.models import db
from app.config import DEFAULT_APP_NAME,DEFAULT_MODULES,HOST,PORT

bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.login_view="user.login"

#create app and config app

def create_app(config_file='config.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file, silent=False)
    bootstrap.init_app(app)
    db.init_app(app)
    for module,url_prefix in DEFAULT_MODULES:
        app.register_blueprint(module, url_prefix=url_prefix)

    return app

