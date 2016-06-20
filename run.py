from app import create_app
from app.subapps.home.routing import homeRoute
from app.subapps.chart_demo.routing import chartRoute
from app.subapps.table_demo.routing import tableRoute
from app.config import HOST,PORT

DEFAULT_MODULES = (
    (homeRoute, ''),
    (chartRoute,'/chart'),
    (tableRoute,'/table')
)

app = create_app('config.py')

for module,url_prefix in DEFAULT_MODULES:
    app.register_blueprint(module, url_prefix=url_prefix)


@app.before_request
def before_request():
    """
    这里是全局的方法，在请求开始之前调用。
    其中 flask 有个全局的变量 g，它是和 session 一样的用途，可以使用它来保存当前用户的数据
    Returns:

    """
    pass


if __name__ == '__main__':
    app.run(host=HOST,port=PORT,threaded=True )