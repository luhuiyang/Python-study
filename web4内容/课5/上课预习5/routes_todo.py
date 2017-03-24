from utils import log
from todo import Todo


def template(name):
    """
    根据名字读取 templates 文件夹里的一个文件并返回
    """
    path = 'templates/' + name
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def response_with_headers(headers, code=200):
    """
    Content-Type: text/html
    Set-Cookie: user=gua
    """
    header = 'HTTP/1.1 {} VERY OK\r\n'.format(code)
    header += ''.join(['{}: {}\r\n'.format(k, v)
                           for k, v in headers.items()])
    return header


def redirect(url):
    """
    浏览器在收到 302 响应的时候
    会自动在 HTTP header 里面找 Location 字段并获取一个 url
    然后自动请求新的 url
    """
    headers = {
        'Location': url,
    }
    # 增加 Location 字段并生成 HTTP 响应返回
    # 注意, 没有 HTTP body 部分
    r = response_with_headers(headers, 302) + '\r\n'
    return r.encode('utf-8')


def index(request):
    """
    todo 首页的路由函数
    """
    headers = {
        'Content-Type': 'text/html',
    }
    todo_list = Todo.all()
    # 下面这行生成一个 html 字符串
    todo_html = ''.join(['<h3>{} : {}</h3>'.format(t.id, t.title) for t in todo_list])
    # 替换模板文件中的标记字符串
    body = template('todo_index.html')
    body = body.replace('{{todos}}', todo_html)
    # 下面 3 行可以改写为一条函数, 还把 headers 也放进函数中
    header = response_with_headers(headers)
    r = header + '\r\n' + body
    return r.encode(encoding='utf-8')


def add(request):
    """
    用于增加新 todo 的路由函数
    """
    headers = {
        'Content-Type': 'text/html',
    }
    if request.method == 'POST':
        form = request.form()
        t = Todo.new(form)
        t.save()
    # 浏览器发送数据过来被处理后, 重定向到首页
    # 浏览器在请求新首页的时候, 就能看到新增的数据了
    return redirect('/todo')

def edit(request):
    """
        编辑旧 todo 的界面
        """

    form = request.form()
    todo_id = request.form[id]
    todo = Todo.find_by(id = todo_id)
    body = template('todo_edit.html', todo=todo)
    headers ={
        'Content-Type': 'text/html',
    }
    header = response_with_headers(headers)
    response = header + '/r/n' + body
    return response.encode(encoding='utf-8')

def update(request):
    """
    编辑微博的路由函数
    :param request:
    """
    todo_id = int(request.query.get('id'))
    t = Todo.find_by(id=todo_id)
    form = request.form()
    t.task = form.get('task')
    t.update_time = form.get('update_time')
    t.save()
    return redirect('/')


# 路由字典

# key 是路由(路由就是 path)
# value 是路由处理函数(就是响应)
route_dict = {
    '/todo': index,
    '/todo/add': add,
    '/todo/edit': edit,
    '/todo/update': update,
}
