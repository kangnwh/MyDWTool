from app.manage import create_app

app = create_app()

@app.before_request
def before_request():
    """
    这里是全局的方法，在请求开始之前调用。
    其中 flask 有个全局的变量 g，它是和 session 一样的用途，可以使用它来保存当前用户的数据
    Returns:
    """
    pass

def run_app():
    app.run(host=app.config.get("HOST","127.0.0.1"),port=app.config.get("PORT","5001"),threaded=True)

if __name__ == '__main__':
    run_app()