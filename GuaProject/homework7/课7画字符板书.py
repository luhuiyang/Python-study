import turtle

t = turtle.Turtle()
# t.speed(0)
# tracer 是关闭动画的
turtle.tracer(10000, 0.0001)

c = {
    'color': 'black',
}


def click(*args):
    print('click')
    print(args)
    x, y = args
    length = 50
    x = (x // length) * length
    y = (y // length + 1) * length
    draw_char(x, y, char_8)


def setpen(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(0)

def rect(x, y, l, color):
    setpen(x, y)
    t.color('red')
    # t.fillcolor(c['color'])
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4):
        t.forward(l)
        t.right(90)
    t.end_fill()


def black():
    print('black')
    c['color'] = 'black'

def white():
    print('white')
    c['color'] = 'white'


# onkey 是说 按某个键的时候 调用你配置的函数
turtle.onkey(black, "Up")
turtle.onkey(white, "Down")




def draw_char(x, y, a):
    length = 10
    for i, row in enumerate(a):
        offset_y = y - i * length
        for j, c in enumerate(row):
            offset_x = x + j * length
            if c == '0':
                color = 'white'
            else:
                color = 'black'
                rect(offset_x, offset_y, length, color)
            print('color', color)
char_1 = [
    '01100',
    '00100',
    '00100',
    '00100',
    '01110',
]

char_8 = [
    '11111',
    '10001',
    '10001',
    '11111',
    '10001',
    '10001',
    '11111',
]

# draw_char(char_8)

turtle.listen()

# onscreenclick 是配置一个函数, 你点击屏幕的时候调用
turtle.onscreenclick(click)


turtle.update()
turtle.done()
