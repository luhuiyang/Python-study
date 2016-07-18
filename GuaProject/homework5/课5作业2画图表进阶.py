# 2016/7/17
#
# ========
# 作业 2
#
# 这次是要写更加具备...
# extensibility     可扩展
# customizability   可定制
# reusability       可重用
# maintainability   可维护
# scalability       可伸缩
# usability         易用
# consistency       一致
# robustness        魯棒
# 性的图表函数


# ========
# 注意, 本次作业基于课 4 作业 1.5
# 请在课 4 作业 1 的文件中增加这些功能
# 鲁棒是古代的翻译, 其实是健壮的意思, 就是说一个函数随便折腾不容易跪
# ========
#
# 注意, 本次作业没有提示
# 下面是要用到的函数

import pen


def axises_wh(x, y, w=300, h=300):
    '''
    以 x, y 为原点画一个坐标轴
    x 轴长为 w, 默认是 300
    y 轴长为 h, 默认是 300

    :param x: 坐标轴原点 x 坐标
    :param y: 坐标轴原点 y 坐标
    :param w: 坐标轴 x 的长度
    :param h: 坐标轴 y 的长度
    :return: None
    '''
    # 无痕移动至原点
    pen.setpen(x, y)
    # 画 x 轴
    pen.goto(x + w, y)
    # 无痕移动至原点
    pen.setpen(x, y)
    # 画 y 轴
    pen.goto(x, y + h)
    pen.setpen(x, y)


def rect_line_sample(x, y, w, h, space, n):
    '''
    横向画一排矩形, x y 是整个矩形排的左上角坐标
    矩形之间的间隔设置为 10
    矩形宽高分别是 50 100

    :param x: 这排矩形的左上角坐标
    :param y: 这排矩形的左上角坐标
    :param n: 矩形的个数
    :return: None
    '''
    # space 表示矩形间的间隙
    # space = 10
    # w h 分别是矩形的宽和高, 可以这样定义变量
    # w, h = 50, 100
    # 矩形的颜色 这里设置为红色
    color = '#ff0000'
    for i in range(n):
        x1 = x + (w + space) * i
        y1 = y
        # 注意, 这里调用的是 pen 模块中的 rect 函数来完成功能
        pen.rect(x1, y1, w, h, color)


# 2.1
# 扩展 1.5 的函数
# 1, 增加 w h 是图表整体的高
# 2, 给图表增加背景色 '#beeeef'
def bar_chart1(x, y, w, h, forecasts, height_ratio = 10, color='#ff0000', space=10, bar_width = 30):
    # 先设置图表属性
    # w, h = 300, 300
    # 画坐标轴
    axises_wh(x, y, w, h)
    #
    # 每度的高度
    # height_ratio = 10
    # 设置一下每个柱子的宽度
    # bar_width = 30
    # 遍历画柱子
    # 注意这个新函数 enumerate, 可以返回 下标 和 元素
    newx = x + space
    maxheight = max(forecasts)
    backgroundheight = maxheight * height_ratio
    for i, temp in enumerate(forecasts):
        offset_x = newx + (bar_width + space) * i
        offset_y = y + backgroundheight
        pen.rect(offset_x, offset_y, bar_width, backgroundheight, '#beeeef')
    for i, temp in enumerate(forecasts):
        offset_x = newx + (bar_width + space) * i
        offset_y = y + temp * height_ratio
        bar_height = offset_y - y
        pen.rect(offset_x, offset_y, bar_width, bar_height, color)

temps = [22, 19, 22, 30, 25, 27, 24]
# 在 0, 0 处画出天气数据
# bar_chart1(-200, -200, 300, 300, temps)


# 2.2
# 扩展 2.1 的函数
# 图表每度不再是 10 像素, 而是根据高度计算出来
# 让图表最大的数据的高度为图表高度的 90%
def bar_chart2(x, y, w, h, forecasts, color='#ff0000', space=10):
    maxNumber = max(forecasts)
    height_ratio = h * 0.9 / maxNumber
    bar_chart1(x, y, w, h, forecasts, height_ratio, color, space)


# bar_chart2(-200, -200, 200, 200, temps)


# 2.3
# 扩展 2.2
# 增加一个参数 scale 代表「图表中最大数据的高度 和 图表高度的比值」
def bar_chart3(x, y, w, h, forecasts, scale=0.9, color='#ff0000', space=10):
    maxNumber = max(forecasts)
    height_ratio = h * scale / maxNumber
    bar_chart1(x, y, w, h, forecasts, height_ratio, color, space)


# bar_chart3(-200, -200, 200, 200, temps, 0.5)



# 2.4
# 扩展 2.3
# 增加一个参数 bar_width 来表示柱子的宽度
def bar_chart4(x, y, w, h, forecasts, bar_width, scale=0.9, color='#ff0000', space=10):
    maxNumber = max(forecasts)
    height_ratio = h * scale / maxNumber
    bar_chart1(x, y, w, h, forecasts, height_ratio, color, space, bar_width)


# bar_chart4(-200, -200, 200, 200, temps, 20, 0.5)

# 2.5
# 扩展 2.4
# 如果用指定的 bar_width 绘图让整个图表超过了指定的宽度
# 那么就减小 bar_width 至能完美贴合
# 完美贴合即: 最后一个柱子的右侧和图表的右边框重合
def bar_chart5(x, y, w, h, forecasts, bar_width, scale=0.9, color='#ff0000', space=10):
    if (w / len(forecasts) - space) < bar_width:
        bar_width = w / len(forecasts) - space
    bar_chart4(x, y, w, h, forecasts, bar_width, scale, color, space)


# bar_chart5(-200, -200, 200, 200, temps, 20, 0.9)


# 2.6
# 扩展 2.5
# 1, 让柱子完美贴合, 间距平均
# 2, 让 space 为最小间距, 意即: 在满足 完美贴合 和 bar_width 的情况下
#    如果 间距 小于 space, 则减小 bar_width, 优先保证 space 的值
# 3, 其他未说明的情况不用考虑
def bar_chart6(x, y, w, h, forecasts, bar_width, scale=0.9, color='#ff0000', space=10):
    if (w / len(forecasts) - bar_width) < space:
        bar_width = w / len(forecasts) - space
    bar_chart4(x, y, w, h, forecasts, bar_width, scale, color, space)

# bar_chart6(-200, -200, 200, 200, temps, 20, 0.9)


# 2.7
# 扩展 2.6
# 加上背景标尺
# 背景标尺是平行于 x 轴的黑色线段, 把图表纵向 6 等分
def bar_chart7(x, y, w, h, forecasts, bar_width, scale=0.9, color='#ff0000', space=10):
    for i in range(6):
        averageh = y / 6
        j = i + 1
        newy = y - j * averageh
        newlen = x + w
        pen.setpen(x, newy)
        pen.goto(newlen, newy)
    bar_chart6(x, y, w, h, forecasts, bar_width, scale, color, space)

bar_chart7(-200, -200, 200, 200, temps, 20, 0.9)

# have fun

pen.done()
