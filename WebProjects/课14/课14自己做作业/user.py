from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import Blueprint
from flask import abort
from flask import session

from models import User

from utils import log

# 创建一个 蓝图对象 并且路由定义在蓝图对象中
# 然后在 flask 主代码中「注册蓝图」来使用
# 第一个参数是蓝图的名字，第二个参数是套路
main = Blueprint('user', __name__)


def current_user():
    uid = session.get('user_id')
    if uid is not None:
        u = User.query.get(uid)
        return u


@main.route('/')
def login_view():
    u = current_user()
    if u is not None:
        return redirect(url_for('weibo.index'))
    return render_template('user_login.html')


@main.route('/register', methods=['POST'])
def register():
    form = request.form
    u = User(form)
    if u.valid():
        log('注册用户', u)
        u.save()
        user = User.query.filter_by(username=u.username).first()
        session['user_id'] = user.id
    else:
        log('注册信息有物', u)
        abort(400)
    # 蓝图中的 url_for 需要加上蓝图的名字，这里是 weibo
    return redirect(url_for('weibo.index'))


@main.route('/login', methods=['POST'])
def login():
    form = request.form
    u = User(form)


    log('username', u)

    user = User.query.filter_by(username=u.username).first()
    log('user有没有', user)

    if user is not None and user.validate_login(u):
        print('登录成功')
        session['user_id'] = user.id
        return redirect(url_for('weibo.index'))
    else :
        print('登录失败')
        abort(400)
    # return redirect(url_for('.login_view'))
