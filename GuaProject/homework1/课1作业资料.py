# 作业 1 资料
# 
# 
# 这表示引入了一个别人写好的东西(术语模块, 很快会讲)
import turtle

# 这样可以得到一个变量 t, 可以对它进行很多操作
# 很快会讲, 现在先用
t = turtle.Turtle()


# 循环的资料
# 在循环体内, 可以通过 i 变量得到当前是第几次循环
# i 在每次循环开始的时候, 都会被赋值为一个新值
# 其实是 range(5) 生成了一个包含了 0 1 2 3 4 这五个数字的序列
# i 每次得到序列中的一个新值
for i in range(5):
    print(i)


# 背景资料
# 画图的画面长宽不知几何
# 原点在窗口的中点
# 往右是 x 轴正向
# 往上是 y 轴正向
# 
# 初始化的状态是箭头在原点 朝右
# 
# 下面介绍一些常用的函数

# 定义一个变量表示步长
step = 50

# 设置画画的速度
# 1 到 9 越来越快
# 0 最快(设计这个参数的人脑袋有问题)
t.speed(0)

# forward 表示向前走
# 刚开始的时候朝右, 并且在坐标 (0, 0)
t.forward(step)

# penup 可以把笔抬起来, 这样往前走就不会画线了
t.penup()
t.forward(step)

# pendown 后又可以画线了
t.pendown()
t.forward(step)

# left 可以往左转, 参数是角度
t.left(90)
t.forward(step)

# setheading 可以设置箭头的朝向, 0 就是朝右, 90 和 -90 的朝向, 自行摸索一下
t.setheading(0)

# pensize 可以改变线条粗细
# 建议不要太大
t.pensize(5)

# pencolor 可以设置颜色, 颜色的具体数值可以通过下面这个网页得到
# http://tool.ganchang.cn/getcolortool.html
# 注意, 参数是一个字符串
color = '#55C2DD'
t.pencolor(color)

# right 可以右转
t.right(30)
t.forward(step)

# position 可以得到当前的坐标
pos = t.position()
print('坐标是, ', pos)

# goto 可以直接走到某个坐标
# 这里是走到 (100, 200) 这个坐标
t.goto(100, 200)

# home 可以回到原点
# 利用 penup 可以无痕回到原点
t.home()

# 隐藏箭头
t.hideturtle()

# 显示箭头
t.showturtle()


# 画完后一定要加上这一句
turtle.done()
