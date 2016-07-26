# 2016/7/24
#
# ========
# 作业 (实时更新)
#
# 注意, 作业会在这里实时更新, 有问题请评论
# 注意, 登录论坛后才有评论功能
# ========
# 7/25 更新 8.12
# 7/25 更新 8.11
#
#
# 请直接在我的代码中更改/添加, 不要新建别的文件


# 重新定义我们的 log 函数
def log(*args):
    # print(*args)
    pass


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


a = [1, 2, 3, 1, 3, 5]
b = [1, 2, 3, 5]


# 作业 8.1
# 5 分钟做不出就看提示
#
def unique(a):
    '''
    a 是一个 list
	返回一个 list, 包含了 a 中所有元素, 且不包含重复元素
    例如 a 是 [1, 2, 3, 1, 3, 5]
    返回 [1, 2, 3, 5]

	:return: list
    '''
    result = []
    add = True
    for i in a:
        add = True
        for j in result:
            if i == j:
                add = False
                break
        if add:
            result.append(i)
        log('unique test', result)
    return result


log(ensure(unique(a) == b, '测试1'))

a = [1, 2, 3, 1, 3, 5, 6, 8]
b = [1, 2, 3, 5, 1, 6, 7]


# 作业 8.2
# 5 分钟做不出就看提示
#
def intersection(a, b):
    '''
    a b 都是 list

    返回一个 list, 里面的元素是同时出现在 a b 中的元素
    这个 list 中不包含重复元素

    :return: list
    '''
    result = []
    # a = unique(a)
    # b = unique(b)
    for i in a:
        for j in b:
            if i == j:
                result.append(j)
        log('intersection test', result)
    result = unique(result)
    log('result', result)
    return result


log(ensure(intersection(a, b), '错误1'))


# 作业 8.3
# 5 分钟做不出就看提示
#
def union(a, b):
    '''
    a b 都是 list

    返回一个 list, 里面的元素是所有出现在 a b 中的元素
    这个 list 中不包含重复元素

    :return: list
    '''
    log('union text', unique(a + b))
    return unique(a + b)


log(ensure(union(a, b) == [1, 2, 3, 5, 6, 8, 7], 'union测试1'))


# 作业 8.4
# 5 分钟做不出就看提示
#
def difference(a, b):
    '''
    a b 都是 list

    返回一个 list, 里面的元素是
    所有在 a 中有 b 中没有的元素
    这个 list 中不包含重复元素

    :return: list
    '''
    result = []
    for i in a:
        add = True
        for j in b:
            if i == j:
                add = False
        if add:
            result.append(i)
            log('8.4 result ', result)
    return result


log(ensure(difference(a, b) == [8], '错误'), '测试8.4')


# 作业 8.5
# 5 分钟做不出就看提示
#
def difference_all(a, b):
    '''
    a b 都是 list

    返回一个 list, 里面的元素是
    所有在 a b 中的非公共元素
    这个 list 中不包含重复元素

    :return: list
    '''
    return difference(a, b) + difference(b, a)


log(ensure(difference_all(a, b) == [8, 7], '错误'), '测试8.4')


# 作业 8.6
# 5 分钟做不出就看提示
#
def issubset(a, b):
    '''
    a b 都是 list

	检查是否 a 中的每个元素都在 b 中出现
    返回 bool

    :return: bool
    '''
    return difference(a, b) == []


# ===
# 下面开始是扫雷的作业了
# ===
# 自行补全所需的代码
# 比如 rect
#
# 作业 8.7
# 5 分钟做不出就看提示
#
import turtle

t = turtle.Turtle()
turtle.tracer(10000, 0.0001)


def setpen(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(0)


def rect(x, y, l, color):
    setpen(x, y)
    t.color('white')
    # t.fillcolor(c['color'])
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4):
        t.forward(l)
        t.right(90)
    t.end_fill()


# def click(*args):
#     print('click')
#     print(args)
#     x, y = args
#     length = 50
#     x = (x // length) * length
#     y = (y // length + 1) * length
#     draw_char(x, y, char_8)



def draw_pixel(x, y, pixel, size=3):
    '''
    pixel 是一个 像素值
    像素值是只有一个字符的 str
    如果是 '0' 则画一个白色否则画黑色

	以坐标 x y 为矩形左上角顶点画一个边长为 size 的正方形

    :return: None
    '''
    color = {
        '0': 'white',
        '1': 'black',
    }
    rect(x, y, size, color[pixel])


# draw_pixel(0, 0, '1', 33)


# 作业 8.8
# 5 分钟做不出就看提示
#
def draw_line(x, y, pixels, size=3):
    '''
    pixels 是一个包含了像素值的 list

	以坐标 x y 为左上角顶点画一排边长为 size 的正方形

    :return: None
    '''
    for i in range(len(pixels)):
        offset_x = x + i * size
        log('offset_x = ', offset_x, 'i = ', i)
        log('pixels[', i, '] = ', pixels[i])
        draw_pixel(offset_x, y, pixels[i], size)


# draw_line(0, 0, ['1', '0', '1','0', '1'], 10)

# 作业 8.9
# 5 分钟
#
def draw_block(x, y, block, size=3):
    '''
    block 是一个包含了 pixels list 的 list
	(也就是一个像素方阵)

	以坐标 x y 为左上角顶点画一个边长为 size 的正方形方阵

    :return: None
    '''
    for i in range(len(block)):
        offset_y = y - i * size
        log('offset_x = ', offset_y, 'i = ', i)
        log('block[', i, '] = ', block[i])
        draw_line(x, offset_y, block[i], size)


block = [
    ['1', '0', '1', '0', '1'],
    ['1', '0', '1', '0', '1'],
    ['1', '0', '1', '0', '1'],
    ['1', '0', '1', '0', '1'],
    ['1', '0', '1', '0', '1'],
]


# draw_block(0, 0, block, 10)




# 作业 8.10
# 5分钟
#
def draw_block_line(x, y, line, size=3):
    '''
    line 是一个包含了上面 block 元素的 list
    block 的宽度是 size * number_of_pixels (这个不懂就留言问)
    x y 是左上角顶点坐标

    :return: None
    '''
    # block = []
    # number = int(line / size)
    # for i in range(number):
    #     temp = []
    #     for j in range(number):
    #         temp.append('0')
    #     block.append(temp)
    # draw_block(x, y, block, size)
    offset = len(line[0][0]) * size
    for i in range(len(line)):
        offset_x = x + offset * i
        draw_block(offset_x, y, line[i], size)


# draw_block_line(-100, 100, [block])


# 作业 8.11
# 5分钟
#
def draw_block_map(x, y, map, size=3):
    '''
    map 是一个包含了 line 元素的 list
    line 是一个包含了上面 block 元素的 list
    map 的宽高是 block_size * number_of_pixels (这个不懂就留言问)
    x y 是左上角顶点坐标

    :return: None
    '''
    offset = len(map[0][0][0]) * size
    for i in range(len(map)):
        offset_y = y - i * offset
        draw_block_line(x, offset_y, map[i], size)

# draw_block_map(-200, -200, [[block]])



        # 作业 8.12


# 5分钟
#
# 画扫雷地图
# 利用作业 7 中 marked_square 生成的 list
square = [
    [1, 2, 9, 2, 9],
    [1, 9, 2, 2, 2],
    [1, 2, 2, 2, 9],
    [1, 2, 9, 2, 1],
    [9, 2, 1, 1, 0],
]

char = {
    0: [
        '00000000000',
        '00000000000',
        '00001110000',
        '00010001000',
        '00010001000',
        '00010001000',
        '00010001000',
        '00010001000',
        '00001110000',
        '00000000000',
        '00000000000',
    ],

    1: [
        '00000000000',
        '00000000000',
        '00000100000',
        '00001100000',
        '00000100000',
        '00000100000',
        '00000100000',
        '00000100000',
        '00001110000',
        '00000000000',
        '00000000000',
    ],

    2: [
        '00000000000',
        '00000000000',
        '00011111000',
        '00000001000',
        '00000001000',
        '00011111000',
        '00010000000',
        '00010000000',
        '00011111000',
        '00000000000',
        '00000000000',
    ],

    3: [
        '00000000000',
        '00000000000',
        '00011111000',
        '00000001000',
        '00000001000',
        '00011111000',
        '00000001000',
        '00000001000',
        '00011111000',
        '00000000000',
        '00000000000',
    ],

    4: [
        '00000000000',
        '00000000000',
        '00000010000',
        '00000110000',
        '00001010000',
        '00010010000',
        '00111111100',
        '00000010000'
        '00000010000',
        '00000010000',
        '00000000000',
    ],

    5: [
        '00000000000',
        '00000000000',
        '00011111000',
        '00010000000',
        '00010000000',
        '00011111000',
        '00000001000',
        '00000001000',
        '00011110100',
        '000000000000',
        '00000000000',
    ],

    6: [
        '00000000000',
        '00000000000',
        '00011111000',
        '00010000000',
        '00010000000',
        '00011111000',
        '00010001000',
        '00010001000',
        '00011111000',
        '00000000000',
        '00000000000',
    ],

    7: [
        '00000000000',
        '00000000000',
        '00011111000',
        '00010001000',
        '00000001000',
        '00000001000',
        '00000001000',
        '00000001000',
        '00000001000',
        '00000000000',
        '00000000000',
    ],

    8: [
        '00000000000',
        '00000000000',
        '00011111000',
        '00010001000',
        '00010001000',
        '00011111000',
        '00010001000',
        '00010001000',
        '00011111000',
        '00000000000',
        '00000000000',
    ],

    9: [
        '00000000000',
        '00000100000',
        '00101110100',
        '00011111000',
        '00110111100',
        '01110111110',
        '00111111100',
        '00011111000',
        '00101110100',
        '00000100000',
        '00000000000',
    ],
}


def draw_mine_map(x, y, map):
    '''
    x y 是地图左上角坐标

    map 是一个 marked_square 生成的 list(如上 square 所示)
    使用之前的函数画出这个地图
    注意: 0 - 8 的字符图案都存在一个 dict 中, 你要定义好
    字符图案最好是 10 * 10 或者 15 * 15, 总之工整一点且必须是正矩形

    :return: None
    '''
    mymap = []
    for i in square:
        tempmap = []
        for j in i:
            tempmap.append(char.get(j))
            # log(char[j])
        mymap.append(tempmap)
    draw_block_map(x, y, mymap, 8)

# 直接使用 square 来调用画地图函数
draw_mine_map(-200, 200, square)

turtle.listen()

# onscreenclick 是配置一个函数, 你点击屏幕的时候调用
# turtle.onscreenclick(click)


turtle.update()
turtle.done()
# =====
# 提示
# =====
'''
暂缺
'''
