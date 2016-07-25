# 2016/7/22
#
# ========
# 作业 (实时更新)
#
# 注意, 作业会在这里实时更新, 有问题请评论
# 注意, 登录论坛后才有评论功能
# ========
# 更新 7.11
#
#
# 请直接在我的代码中更改/添加, 不要新建别的文件

# import 后面要用到的生成随机数的模块
import random
import turtle


# 又一次重新定义我们的 log 函数


def log(*args):
    print(*args)


# ====
# 测试
# 如果没有测试, 自行编写
# ====
#
# 定义我们用于测试的函数
# ensure 接受两个参数
# condition 是 bool, 如果为 False, 则输出 message
# 否则, 不做任何处理
def ensure(condition, message):
    # 在条件不成立的时候, 输出 message
    if not condition:
        log('*** 测试失败:', message)


# 作业 7.1
# 11 分钟做不出就看提示
#
def range1(start, end):
    '''
    start end 都是数字

    使用 while 循环
    返回一个 list, 假设 start 为 1, end 为 5, 返回数据如下
    [1, 2, 3, 4]

    :return: list
    '''
    # log('range1', [i for i in range(start, end)])
    # return [i for i in range(start, end)]
    i = start
    list = []
    while i < end:
        list.append(i)
        i += 1
    log(list)
    return list


log(ensure(range1(1, 5) == [1, 2, 3, 4], 'range1 测试1'))


# 作业 7.2
# 8 分钟做不出就看提示
#
def range2(start, end, step=1):
    '''
    start end step 都是数字

    使用 while 循环
    返回一个 list
    假设 start=1, end=5, step=1 返回数据如下
    [1, 2, 3, 4]
    假设 start=0, end=6, step=2 返回数据如下
    [0, 2, 4]

    :return: list
    '''

    # log('range2', [i for i in range(start, end, step)])
    # return [i for i in range(start, end, step)]
    i = start
    list = []
    while i < end:
        list.append(i)
        i += step
    log(list)
    return list


log(ensure(range2(0, 6, 2) == [0, 2, 4], 'range2 测试1'))


# 作业 7.3
# 8 分钟做不出就看提示
#
def range3(start, end, step=1):
    '''
    start end step 都是数字

    和 7.2 一样, 但是要求支持负数 step
    使用 while 循环
    返回一个 list
    假设 start=1, end=5, step=1 返回数据如下
    [1, 2, 3, 4]
    假设 start=6, end=0, step=-1 返回数据如下
    [6, 5, 4, 3, 2, 1]

    :return: list
    '''
    i = start
    list = []
    while abs(i - end) >= 1:
        list.append(i)
        i += step
    log(list)
    return list


log(ensure(range3(6, 0, -1) == [6, 5, 4, 3, 2, 1], 'range3 测试1'))
log(ensure(range3(1, 5, 1) == [1, 2, 3, 4], 'range3 测试2'))


# 作业  7.4
# 10 分钟
#
# 随机模块生成随机 int 的使用方法如下(包含 0 1)
# random.randint(0, 1)
def random_line_01(n):
    '''
    返回一个只包含了 0 1 的随机 list, 长度为 n
    假设 n 为 5, 返回的数据格式如下(这是格式范例, 真实数据是随机的)
    [0, 0, 1, 0, 1]

    :param n: int, 代表 list 长度
    :return: 包含了随机 0 1 的 list
    '''
    log('random_line_01', [random.randint(0, 1) for i in range(n)])
    return [random.randint(0, 1) for i in range(n)]


random_line_01(9)


# 作业  7.5
# 10 分钟
#
def random_square_01(n):
    '''
    返回以下格式的数据
    假设 n 为 3, 返回的数据格式如下(这是格式范例, 真实数据是随机的)
    注意, 这只是一个 list, 并不是它显示的样子
    注意, 这是一个 list 不是 str
    [
        [0, 0, 1],
        [1, 0, 1],
        [0, 0, 0],
    ]
    :param n: int
    :return: 包含了 n 个『只包含 n 个「随机 0 1」的 list』的 list
    '''
    log('random_square_01()', [random_line_01(n) for i in range(n)])
    return [random_line_01(n) for i in range(n)]


random_square_01(3)


# 作业  7.6
# 6 分钟
#
def random_line_09(n):
    '''
    返回一个只包含了 0 9 的随机 list, 长度为 n
    假设 n 为 5, 返回的数据格式如下(这是格式范例, 真实数据是随机的)
    [0, 0, 9, 0, 9]

    :param n: int, 代表 list 长度
    :return: 包含了随机 0 9 的 list
    '''
    return 9 * random_line_01(n)


# 作业  7.7
# 5 分钟
#
def marked_line(array):
    '''
    array 是一个只包含了 0 9 的 list
    返回一个标记过的 list
    ** 注意, 使用一个新数组来存储结果, 不要直接修改老数组

    标记规则如下
    对于下面这样的 array
    [0, 0, 9, 0, 9]
    标记后是这样
    [0, 1, 9, 2, 9]

    规则是, 0 会被设置为左右两边 9 的数量

    :param array: list
    :return: 标记后的 array
    '''
    a = [0] + array + [0]
    log('a = ', a)
    for i in range(len(a)):
        if a[i] == 9:
            a[i + 1] += 1
            a[i - 1] += 1
    return a[1:-1]


log('marked_line', marked_line([0, 0, 9, 0, 9]))
print(ensure(marked_line([0, 0, 9, 0, 9]) == [0, 1, 9, 2, 9], 'marked_line 测试1'))

# 作业 7.8
# 15 分钟

t = turtle.Turtle()


def setpen(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(0)


def radius_coner(radius=20):
    '''
    画一个 90 度的圆角(也就是 1/4 圆), 圆角的半径为 r
    思路是用半径算出 1/4 圆周, 多边形近似的方法
    我们用正 36 边形来模拟圆周
    :param radius: 圆角的半径
    :return: None
    '''
    PI = 3.1415926535
    c = 2 * PI * radius
    step = c / 36
    angle = 360 / 36
    for i in range(int(36 / 4)):
        t.forward(step)
        t.right(angle)


# radius_coner(50)


# 作业 7.9
# 15 分钟
def rect_radius(x, y, w, h, radius=10, color='black'):
    '''
    画一个矩形, 和之前的一样
    多了一个 radius 参数
    这个参数指定了矩形的圆角半径
    一个矩形有 4 个角, 圆角半径的意思是矩形的四个角
    都是 7.8 中所说的 90 度圆角

    :param x: 矩形左上角的 x
    :param y: 矩形左上角的 y
    :param w: 矩形的 宽
    :param h: 矩形的 高
    :param radius: 圆角的半径
    :param color: 矩形的填充色
    :return: None
    '''
    setpen(x, y)
    for i in range(2):
        t.forward(w)
        radius_coner(radius)
        t.forward(h)
        radius_coner(radius)


# rect_radius(0, 0, 30, 40)



# 作业 7.10
# 20 分钟
#
def marked_square(array):
    '''
    array 是一个「包含了『只包含了 0 9 的 list』的 list」
    返回一个标记过的 list
    ** 注意, 使用一个新数组来存储结果, 不要直接修改老数组

    范例如下, 这是 array
    [
        [0, 9, 0, 0],
        [0, 0, 9, 0],
        [9, 0, 9, 0],
        [0, 9, 0, 0],
    ]

    这是标记后的结果
    [
        [1, 9, 2, 1],
        [2, 4, 9, 2],
        [9, 4, 9, 2],
        [2, 9, 2, 1],
    ]

    规则是, 0 会被设置为四周 8 个元素中 9 的数量

    :param array: list
    :return: 标记后的 array
    '''
    margin = [0 for i in array]
    newarray = []
    newarray.append(margin)
    newarray += array
    newarray.append(margin)
    array = newarray
    log('margin', array)

    for i, temp in enumerate(array):
        temp_list = array[i]
        log('temp_list', temp_list)
        array[i] = [0] + temp_list + [0]
    log('added_array ', array)
    for j in range(1, len(array) - 1):
        item = array[j]
        log('j = ', j)
        item = marked_line(item)
        log('markedline ', j, ' = ', item)
        for k in range(1, len(item) - 1):
            log('k = ', k)
            if item[k] != 9:
                if (array[j - 1][k] == 9):
                    item[k] += 1
                if (array[j + 1][k] == 9):
                    item[k] += 1
                if (array[j - 1][k - 1] == 9):
                    item[k] += 1
                if (array[j + 1][k - 1] == 9):
                    item[k] += 1
                if (array[j - 1][k + 1] == 9):
                    item[k] += 1
                if (array[j + 1][k + 1] == 9):
                    item[k] += 1
        array[j] = item
        log('result arrayjjjj ', array[j])
    for index, item in enumerate(array):
        item = item[1:-1]
        array[index] = item
    log('result array ', array[1:-1])
    return array[1:-1]


array = [
    [0, 9, 0, 0],
    [0, 0, 9, 0],
    [9, 0, 9, 0],
    [0, 9, 0, 0],
]

marked_square(array)


# 作业 7.11
# 10 分钟
#
def random_square_09(n, limit=3):
    '''
    返回以下格式的数据
    只包含 0 和 9
    limit 是 9 的个数
    假设 n 为 4, 返回的数据格式如下(这是格式范例, 真实数据是随机的)
    注意, 这只是一个 list, 并不是它显示的样子
    注意, 这是一个 list 不是 str
    [
        [0, 9, 0, 0],
        [0, 0, 9, 0],
        [9, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    :param n: int
    :return: 包含了 n 个『只包含 n 个「随机 0 9」的 list』的 list, 9 的个数是 limit
    '''
    nine_count = 0
    result = []
    for i in range(n):
        list = []
        for j in range(n):
            if nine_count != limit:
                temp = random.randint(0, 1) * 9
                if temp == 9:
                    nine_count += 1
            else:
                temp = 0
            list.append(temp)
        result.append(list)
    log("random_square_09", result)
    return result


random_square_09(4, 3)

turtle.done()

# =====
# 提示
# =====
'''
7.1
range1
    while 循环设置好终止条件往 list 中添加元素


7.2
range2
    同 7.1


7.3
range3
    处理的时候, 需要注意负数的情况


7.4
random_line_01
    循环生成随机数字添加到 list


7.5
random_square_01
    直接使用 7.4


7.6
random_line_09
    7.4 的小小变种


7.7
marked_line
    要用下标来遍历 list
    这样就能方便地访问左右了


7.8
radius_coner
    算出圆周, 就能算出每 10 度的步长
    然后循环走 9 步, 每次转 10 度就好了
    因为我们是用正 36 边形模拟, 所以 1/4 圆周就是 9 步


7.9
rect_radius
    根据 7.8, 需要纸上模拟计算一下圆角矩形


7.10
marked_square
    用 enumerate 来遍历, 可以得到下标和元素
    处理好边界条件
    最好双重循环来做
    这题不会的话 可以跳过


7.11
random_square_09
    用一个数字记录已经生成的 9 的个数
    如果达到 limit 就 break
'''
