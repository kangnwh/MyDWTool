# -*- coding:utf-8 -*-
from flask import Flask
from flask_login import LoginManager
# from myreport.common import db

DEFAULT_APP_NAME='MyECharts'

login_manager = LoginManager()
login_manager.login_view="user.login"



def create_app(config_file):
    app = Flask(__name__)
    login_manager.init_app(app)
    # db.init_app(app)
    app.config.from_pyfile(config_file, silent=False)
    return app


def config_db(app):
	# db.init_app(app)
    pass