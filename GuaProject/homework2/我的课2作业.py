# 作业 2 作业
#
#
import turtle

# 这是套路
t = turtle.Turtle()


# 无痕设置画笔位置的辅助函数
def setpen(x, y):
    # 这三行的意思是 移动到 x y 处
    # 但是不露痕迹 (参考资料)
    t.penup()
    t.goto(x, y)
    t.pendown()
    # 设置朝向, 确保箭头朝向 右边
    # 如果是用 t.goto 来画的话, 就不用关心朝向
    t.setheading(0)


# 背景资料
# 介绍一些额外的函数用来填充颜色
# 作业中会用到
# 关于颜色, 请参考作业 1 的资料

# 填充颜色的方法
# x y
# length 边长
# color 填充颜色
def colored_square(x, y, length, color):
    setpen(x, y)
    # 设置画笔颜色和填充色一致, 这样就不会有边框了
    t.pencolor(color)
    # 设置填充颜色
    t.fillcolor(color)
    # 开始填充
    t.begin_fill()
    for i in range(4):
        t.forward(length)
        t.right(90)
    # 结束填充
    # 在开始填充和结束填充之间的点会组成一个多边形并填色
    # 具体请自行尝试
    t.end_fill()


# 这个颜色为红色, 颜色代码请参考作业 1 的资料
# colored_square(0, 0, 100, '#ff0000')




# 作业开始

# 1
# 实现一个矩形函数
# x y 是矩形左上角坐标
# w h 是宽高
# color 是矩形的颜色
# def rect(x, y, w, h, color)
def set_color(color):
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()


def rect(x, y, w, h, color):
    setpen(x, y)
    set_color(color)
    for i in range(2):
        t.forward(w)
        t.right(90)
        t.forward(h)
        t.right(90)

    t.end_fill()


# rect(-100, 100, 200, 100, '#ff0000')

# 2
# 实现一个矩形函数
# x y 是矩形中心的坐标
# w h 是宽高
# color 是矩形的颜色
# def center_rect(x, y, w, h, color)

def center_rect(x, y, w, h, color):
    x = x - w / 2
    y = y + h / 2
    rect(x, y, w, h, color)


# center_rect(0, 0, 200, 100, '#ff0000')

# 3
# 实现一个圆形函数
# x y 是圆心坐标
# r 是半径
# color 是填充色
# def circle(x, y, r, color)
#
# 提示, 我们以正 36 形为圆

def circle(x, y, r, color):
    y = y + r
    set_color(color)
    PI = 3.1415926535
    c = 2 * PI * r
    step = c / 36
    angle = 360 / 36
    x = x - step / 2
    setpen(x, y)
    for i in range(36):
        t.forward(step)
        t.right(angle)

    t.end_fill()


# circle(0, 0, 100, '#ff0000')


# 4
# 实现一个五角星函数
# x y 是五角星横边左边坐标
# length 是一条线的长度
# color 是填充色
# def wujcxy(x, y, length, color)

def wujcxy(x, y, length, color):
    setpen(x, y)
    set_color(color)
    for i in range(5):
        t.forward(length)
        t.left(72)
        t.forward(length)
        t.right(144)
    t.end_fill()


# wujcxy(0, 0, 30, '#ff00ff')

# 5
# 实现一个函数画日本国旗
# 调用 2 个函数画日本国旗
# 一个画背景的白色矩形
# 一个画中间的红色圆
# def japan()

def japan(x, y, h):
    center_rect(x, y, h * 2 + 2, h + 2, '#000000')
    center_rect(0, 0, h * 2, h, '#ffffff')
    circle(0, 0, h / 3, '#ff0000')


# japan(0, 0, 200)
#
# 注意, 你可以添加 x y w h 参数让国旗画在任意地方, 任意尺寸
# 注意, 以下所有国旗同理

# 6
# 实现一个函数画中国国旗(以下国旗题目都是如此 不重复了)
# 调用 2 个函数画中国国旗
# 一个画红色背景
# 另一个画五角星（调用 5 次，不要求角度朝向，只要5个五角星即可）
# def china()
def china(x, y, h):
    center_rect(x, y, h * 2 + 2, h + 2, 'red')
    wujcxy(x - h / 3 * 2, x + h / 4, h / 6, "yellow")
    for i in range(4):
        wujcxy(x - (i * (h / 10)), x + h / 4 - (i * (h / 10)), h / 20, "yellow")


# china(0, 0, 200)

# 7
# 实现一个函数画法国国旗
# def france()
def france(x, y, h, color1='blue', color2='white', color3='red'):
    rect(x, y, h * 2 / 3, h, color1)
    rect(x + h * 2 / 3, y, h * 2 / 3, h, color2)
    rect(x + 2 * h * 2 / 3, y, h * 2 / 3, h, color3)


# france(0, 0, 100)


# 8
# 画德国国旗
# def germany()

def germany(x, y, h, color1='black', color2='red', color3='yellow'):
    rect(x, y, h * 2, h * 2 / 6, color1)
    rect(x, y - h * 2 / 6, h * 2, h * 2 / 6, color2)
    rect(x, y - 2 * h * 2 / 6, h * 2, h * 2 / 6, color3)


# germany(0, 0, 100)

# 9
# 画 冈比亚国旗
# def gambia()
def gambia(x, y, h, color1='red', color2='blue', color3='green'):
    rect(x, y, h * 2, h * 2 / 6, color1)
    rect(x, y - h * 2 / 6, h * 2, (h * 2 / 6 - (h * 2 / 7)) / 2, "white")
    rect(x, y - h * 2 / 6 - ((h * 2 / 6) - (h * 2 / 7)) / 2, h * 2, h * 2 / 6 - (h * 2 / 6 - (h * 2 / 7)), color2)
    rect(x, y - 2 * h * 2 / 6 + ((h * 2 / 6) - (h * 2 / 7)) / 2, h * 2, (h * 2 / 6 - (h * 2 / 7)) / 2, 'white')
    rect(x, y - 2 * h * 2 / 6, h * 2, h * 2 / 6, color3)


# gambia(0, 0, 100)
# 10
# 画 瑞士国旗
# def switzerland()

def switzerland(x, y, h):
    center_rect(x, y, h, h, "red")
    center_rect(x, y + h / 5, h / 5, h / 5, 'white')
    center_rect(x - h / 5, y, h / 5, h / 5, 'white')
    center_rect(x, y, h / 5, h / 5, 'white')
    center_rect(x + h / 5, y, h / 5, h / 5, 'white')
    center_rect(x, y - h / 5, h / 5, h / 5, 'white')


# switzerland(0, 0, 200)

# 11
# 画朝鲜国旗
# 分别是 圆 矩形 五角星
# 提示, 使用之前定义的函数
# def northkorea()
def northkorea(x, y, h):
    rect(x, y, h * 2, h / 5, 'blue')
    rect(x, y - h / 5, h * 2, h / 20, 'white')
    rect(x, y - h / 5 - h / 20, h * 2, h / 2, "red")
    rect(x, y - h + h / 5 + h / 20, h * 2, h / 20, 'white')
    rect(x, y - h + h / 5, h * 2, h / 5, 'blue')
    circle(h / 2, - h / 2, h / 5, "white")
    wujcxy(h / 2 - h / 5 + h / 60, - h / 2 + h / 15, h / 7, 'red')


# northkorea(0, 0, 200)

# 12
# 画出美国国旗
# 美国国旗是 13 条横杠 加上 50 颗星星
#
# 这题做不出拉倒

def wujcxy5(x, y, h):
    # length = (h - h / 13) / 6 / 4
    length = h / 6 / 4
    y = y - length
    for i in range(6):
        hight = y - i * h / 6
        wujcxy(x, hight, length, 'white')


def wujcxy4(x, y, h):
    # length = (h - h / 13) / 6 / 4
    length = h / 6 / 4
    y = y - length
    for i in range(5):
        hight = y - i * h / 6
        wujcxy(x, hight, length, 'white')


def america(x, y, h):
    hight = h / 13
    width = h * 2
    for i in range(7):
        each_hight = y - i * h / 13 * 2
        rect(x, each_hight, width, hight, "red")

    blue_width = h * 5 / 6
    blue_hight = h / 13 * 7
    rect(x, y, blue_width, blue_hight, 'blue')
    for i in range(6):
        wujx = x + i * h / 13 * 2 + blue_hight / 13
        wujxY = y - blue_hight / 13
        wujcxy5(wujx, wujxY, blue_hight)
    for i in range(5):
        wujx = x + i * h / 13 * 2 + blue_hight / 6 + blue_hight / 13
        wujxY = y - blue_hight / 6 / 2 - blue_hight / 13
        wujcxy4(wujx, wujxY, blue_hight)


america(0, 0, 200)

# 画完后一定要加上这一句
# 这句在整个文件的最后面
turtle.done()
