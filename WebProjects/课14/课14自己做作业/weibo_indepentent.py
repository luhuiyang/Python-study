from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from utils import log

# 初始化Flask实例
app = Flask(__name__)


# 定义路由和路由处理函数
# 用 app.route 函数定义路由，参数是一个 path 路径
# 下一行紧跟着的是处理这个请求的函数
# @ 是一个叫装饰器的东西，套路，暂时不用管原理，会用就好
# 注意 method 的参数是一个 list, 规定了这个函数只能接受的 HTTP 方法，不设置的话默认是 GET
@app.route('/weibo', methods=['GET'])
def weibo_index():
    return render_template('weibo_index.html')


# 运行服务器
if __name__ == '__main__':
    # debug 模式可以自动加载你对代码的变动, 所以不用重启程序
    # host 参数指定为 '0.0.0.0' 可以让别的机器访问你的代码
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=2000,
    )
    app.run(**config)
    # app.run() 开始运行服务器
    # 所以你访问下面的网址就可以打开网站了
    # http://127.0.0.1:2000/
