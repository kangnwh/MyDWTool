from app.db_info import connect_str
from app.subapps.home.routing import homeRoute
from app.subapps.chart_demo.routing import chartRoute
from app.subapps.table_demo.routing import tableRoute
from app.subapps.stock.routing import stockRoute


DEBUG = True
SQLALCHEMY_ECHO = False
SQLALCHEMY_DATABASE_URI = connect_str
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = '*\xff\x93\xc8w\x13\x0e@3\xd6\x82\x0f\x84\x18\xe7\xd9\\|\x04e\xb9(\xfd\xc3'
ADMIN_USER = 'admin'
ADMIN_PASSWD = 'passw0rd'
DEFAULT_APP_NAME='MyECharts'
PORT=5001
HOST='127.0.0.1'

DEFAULT_MODULES = (
    (homeRoute, ''),
    (chartRoute,'/chart'),
    (tableRoute,'/table'),
    (stockRoute,'/stock'),
)

