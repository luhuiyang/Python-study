import turtle


# 这个模块实现了 3 个函数
# rect
# center_rect

t = turtle.Turtle()


def setpen(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(0)


def goto(x, y):
    t.goto(x, y)


def done():
    '''
    画图结束后, 必须调用本函数
    '''
    turtle.done()


def rect(x, y, w, h, color):
    '''
    以 x, y 为左上角顶点画一个矩形

    :param x: 矩形左上角坐标 x
    :param y: 矩形左上角坐标 y
    :param w: 矩形宽
    :param h: 矩形高
    :param color: 矩形的颜色

    :return: None
    '''
    # 移动画笔到起点
    setpen(x, y)
    # 设置颜色
    t.pencolor(color)
    t.fillcolor(color)
    # 开始填充
    t.begin_fill()
    t.goto(x + w, y)
    t.goto(x + w, y - h)
    t.goto(x, y - h)
    t.goto(x, y)
    t.end_fill()


def rect_lb(x, y, w, h, color):
    '''
    以 x, y 为左下角顶点画一个矩形
    函数名是 rect left bottom 的意思

    :param x: 矩形左下角坐标 x
    :param y: 矩形左下角坐标 y
    :param w: 矩形宽
    :param h: 矩形高
    :param color: 矩形的颜色

    :return: None
    '''
    rect(x, y+h, w, h, color)

# 使用例子
# rect_lb(0, 0, 100, 200, '#ff0000')
# 画一个左下角在 0, 0  宽 100 高 200 的红色矩形
#