# 16/7/6

import turtle

t = turtle.Turtle()
# 井号开头的内容是注释, 不会被程序识别
# 上面几行是套路, 不用关心

# 例子 1
# 画一个边长为 100 像素的正三角形
# t.forward(100)
# t.right(120)
# t.forward(100)
# t.right(120)
# t.forward(100)
# t.right(120)


# 以下 10 题
# 不考虑图像是否重合等问题
# 只考察是否有实现功能
# 
# 作业 1
# 画一个边长为 10 像素的正三角形
# t.forward(10)
# t.right(120)
# t.forward(10)
# t.right(120)
# t.forward(10)

# 作业 2
# 画一个边长为 99 像素的正方形
# t.forward(99)
# t.right(90)
# t.forward(99)
# t.right(90)
# t.forward(99)
# t.right(90)
# t.forward(99)

# 作业 3
# 画一个长宽分别为 168, 99 像素的矩形
# t.forward(168)
# t.right(90)
# t.forward(99)
# t.right(90)
# t.forward(168)
# t.right(90)
# t.forward(99)

# 作业 4
# 画一个边长为 33 像素的正三角形
# t.left(60)
# t.forward(33)
# t.right(120)
# t.forward(33)
# t.right(120)
# t.forward(33)

# 作业 5
# 画一个边长为 106 像素的正方形
# t.left(45)
# t.forward(106)
# t.left(90)
# t.forward(106)
# t.left(90)
# t.forward(106)
# t.left(90)
# t.forward(106)

# 作业 6
# 画一个长宽分别为 68, 59 像素的矩形
# t.left(90)
# t.forward(59)
# t.right(90)
# t.forward(68)
# t.right(90)
# t.forward(59)
# t.right(90)
# t.forward(68)

# 作业 7
# 画一个边长为 79 的正五边形
# t.forward(79)
# t.left(360 / 5)
# t.forward(79)
# t.left(360 / 5)
# t.forward(79)
# t.left(360 / 5)
# t.forward(79)
# t.left(360 / 5)
# t.forward(79)

# 作业 8
# 画一个边长为 63 的正六边形
# t.right(30)
# t.forward(63)
# t.right(60)
# t.forward(63)
# t.right(60)
# t.forward(63)
# t.right(60)
# t.forward(63)
# t.right(60)
# t.forward(63)
# t.right(60)
# t.forward(63)

# 作业 9
# 画一个边长为 159 的正七边形
# t.right(180)
# t.forward(159)
# t.right(360 / 7)
# t.forward(159)
# t.right(360 / 7)
# t.forward(159)
# t.right(360 / 7)
# t.forward(159)
# t.right(360 / 7)
# t.forward(159)
# t.right(360 / 7)
# t.forward(159)
# t.right(360 / 7)
# t.forward(159)

# 作业 10
# 画一个边长为 93 的正十边形
# t.forward(93)
# t.right(360 / 10)
# t.forward(93)
# t.right(360 / 10)
# t.forward(93)
# t.right(360 / 10)
# t.forward(93)
# t.right(360 / 10)
# t.forward(93)
# t.right(360 / 10)
# t.forward(93)
# t.right(360 / 10)
# t.forward(93)
# t.right(360 / 10)
# t.up()
# t.forward(93)
# t.right(360 / 10)
# t.forward(93)
# t.right(360 / 10)
# t.down()
# t.forward(93)
# turtle.done()

r = 100
t.circle(r)
# t.up()
t.goto(0, (80))
t.down()
t.circle(80)

# 下面一行也是套路, 不用关心
turtle.done()
