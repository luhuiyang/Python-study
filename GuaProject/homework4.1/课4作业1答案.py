# 2016/7/15
#
# ========
# 作业 1 答案
# ========
#
# 请以之前 3 课的资料和作业作为参考
#
# 请直接在我的代码中更改/添加, 不要新建别的文件


# 导入 log
from utils import log

# 导入我们自己的画图模块
# 请仔细阅读 pen.py 的内容
import pen


# 例子 1.1
# 画一排矩形
def rect_line_sample(x, y, n):
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
    space = 10
    # w h 分别是矩形的宽和高, 可以这样定义变量
    w, h = 50, 100
    # 矩形的颜色 这里设置为红色
    color = '#ff0000'
    for i in range(n):
        x1 = x + (w + space) * i
        y1 = y
        # 注意, 这里调用的是 pen 模块中的 rect 函数来完成功能
        pen.rect(x1, y1, w, h, color)


# 例子 1.2
# 画坐标轴
def axises(x, y, length=300):
    '''
    以 x, y 为原点画一个坐标轴
    轴长为 length, 默认是 300

    :param x: 坐标轴原点 x 坐标
    :param y: 坐标轴原点 y 坐标
    :param length: 坐标轴长度
    :return: None
    '''
    # 无痕移动至原点
    pen.setpen(x, y)
    # 画 x 轴
    pen.goto(x + length, y)
    # 无痕移动至原点
    pen.setpen(x, y)
    # 画 y 轴
    pen.goto(x, y + length)

# 用法
#
# 画一个坐标轴在 0 0 处, 长度为默认的 100
# axises(0, 0)
#
# 画一个坐标轴在 -100 -100 处, 长度为 50
# axises(-100, -100, 50)




# 作业 1.1
# 实现 pen.py 中的 rect_lb 函数
# 10 分钟做不出就看提示
# 注意, 在 pen.py 中实现, 不要在这里实现


# 作业 1.2
# 画坐标轴
# 10 分钟做不出就看提示
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


# 作业 1.3
# 实现以下函数, 用来绘制 天气数据折线图
# 折线的颜色任选
# 注意, 不需要坐标轴, 有图表就行
# 10 分钟做不出就看提示
def line_chart(x, y, forecasts, space=50):
    '''
    根据一周天气，绘制天气折线图
    设温度的每度高为 10 像素

    :param x: 图的左下角坐标 x 值
    :param y: 图的左下角坐标 y 值
    :param forecasts: 一周天气数据, 是一个包含 7 个数字的 list
    :param space: 每两个数据之间的间隔, 默认 50
    :return:
    '''
    # 每度的高度
    height_ratio = 10
    # 先把画笔移动到第一个点
    offset_x = x
    offset_y = y + forecasts[0] * height_ratio
    pen.setpen(offset_x, offset_y)
    # 再遍历画线, 第一个点是重复的, 所以用切片删掉
    for d in forecasts[1:]:
        offset_x += 50
        offset_y = y + d * height_ratio
        pen.goto(offset_x, offset_y)


# 用法
# 假设中国本周一到周日的每日平均气温如下
# temps = [22, 19, 22, 30, 25, 27, 24]
# 在 0, 0 处画出天气数据
# line_chart(0, 0, temps)


# 作业 1.4
# 实现以下函数, 给 line_chart 添加一个 w h 为 300 300 的坐标轴
# 10 分钟做不出就看提示
def line_chart2(x, y, forecasts, space=50):
    # 先设置图表属性
    w, h = 300, 300
    # 画坐标轴
    axises_wh(x, y, w, h)
    #
    # 每度的高度
    height_ratio = 10
    # 先把画笔移动到第一个点
    offset_x = x
    offset_y = y + forecasts[0] * height_ratio
    pen.setpen(offset_x, offset_y)
    # 再遍历画线, 第一个点是重复的, 所以用切片删掉
    for temp in forecasts[1:]:
        offset_x += 50
        offset_y = y + temp * height_ratio
        pen.goto(offset_x, offset_y)

# 测试一下
# temps = [22, 19, 22, 30, 25, 27, 24]
# line_chart2(0, 0, temps)


# 题 1.5
# 实现以下函数, 用来绘制 天气预报柱状图
# 注意, 要添加坐标轴, 轴的 w h 分别为 300 300
# 10 分钟做不出就看提示
def bar_chart(x, y, forecasts, color='#ff0000', space=10):
    '''
    画一个柱状图
    设温度的每度高为 10 像素

    :param x: 整个柱状图的左下角坐标 x
    :param y: 整个柱状图的左下角坐标 y
    :param forecasts: 一周天气数据, 是一个包含 7 个数字的 list
    :param color: 矩形柱的颜色, 默认 '#ff0000'
    :param space: 每两个矩形柱之间的间隔, 默认 10
    :return:
    '''
    # 先设置图表属性
    w, h = 300, 300
    # 画坐标轴
    axises_wh(x, y, w, h)
    #
    # 每度的高度
    height_ratio = 10
    # 设置一下每个柱子的宽度
    bar_width = 30
    # 遍历画柱子
    # 注意这个新函数 enumerate, 可以返回 下标 和 元素
    for i, temp in enumerate(forecasts):
        offset_x = x + (bar_width + space) * i
        offset_y = y + temp * height_ratio
        bar_height = offset_y - y
        pen.rect(offset_x, offset_y, bar_width, bar_height, '#000000')



# 用法
# 假设中国本周一到周日的每日平均气温如下
temps = [22, 19, 22, 30, 25, 27, 24]
# 在 0, 0 处画出天气数据
bar_chart(0, 0, temps)



# 最后要调用 pen.done()
pen.done()
