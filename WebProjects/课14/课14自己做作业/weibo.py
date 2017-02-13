from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import abort
from utils import log


from user import current_user
from models import Weibo
from models import Comment

# 创建一个 蓝图对象，并且路由定义在蓝图对象中
# 然后在 flask 主代码中[注册蓝图]来使用
# 第一个参数是蓝图的名字，第二个参数是套路
main = Blueprint('weibo', __name__)


@main.route('/')
def index():
    # 查找所有微博
    weibo_list = Weibo.query.all()
    comment_list = Comment.query.all()
    return render_template('weibo_index.html', weibos=weibo_list, comments=comment_list)

@main.route('/add', methods=['POST'])
def add():
    form = request.form
    log('打印了什么', form)
    u = current_user()
    if u is not None:
        w = Weibo(form, u.id)
        if w.valid():
            w.save()
        else :
            abort(400)
        # 蓝图中的 url_for 需要加上蓝图的名字，这里是weibo 可以理解为weibo这个蓝图的index
        return redirect(url_for('weibo.index'))
    else :
        log('日志', '用户未登录')


@main.route('/comment', methods=['POST'])
def comment():
    form = request.form
    log('打印了什么', form)
    u = current_user()
    if u is not None:
        c = Comment(form, u.id)

        if u.valid():
            u.save()
        else :
            abort(400)
            # 蓝图中的 url_for 需要加上蓝图的名字，这里是weibo 可以理解为weibo这个蓝图的index
        return redirect(url_for('weibo.index'))
    else :
        log('日志', '用户未登录')


# @main.route('/')
