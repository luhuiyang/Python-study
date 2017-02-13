from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for

from weibo import main as weibo_routes
from user import main as user_routes

app = Flask(__name__)

# 设置 secret_key 来使用 flask 自带的 session
# 这个字符串随便设置什么内容
app.secret_key = 'honey'
# 这一行是套路
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

'''
在 flask 中，模块化的路由功能有 蓝图（Blueprints）提供
蓝图可以拥有自己的静态路由资源路径、模板路径（现在还没有设计）
用法如下
'''

# 注册蓝图
# 有一个 url_prefix 可以用来给蓝图中的没一个路由加一个前缀
app.register_blueprint(weibo_routes, url_prefix='/weibo')
app.register_blueprint(user_routes, url_prefix="/user")


@app.errorhandler(404)
def error404(e):
    return render_template('404.html')


@app.route('/')
def redirect_to_login():
    return redirect(url_for('user.login_view'))
    # return redirect(url_for('weibo.index'))

# 运行代码
# 默认端口是 5000
if __name__ == '__main__':
    app.run(debug=True)