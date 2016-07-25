# # 例子 1
# def draw_char(x, y, a):
#     length = 1
#     for i, row in enumerate(a):
#         offset_y = y - i * length
#         for j, c in enumerate(row):
#             offset_x = x + j * length
#             if c == '0':
#                 color = 'white'
#             elif c == '1':
#                 color = 'black'
#                 rect(offset_x, offset_y, length, color)
#             elif c == '2':
#                 color = 'red'
#                 rect(offset_x, offset_y, length, color)
#             elif c == '3':
#                 color = '#CCCCCC'
#                 rect(offset_x, offset_y, length, color)
#             elif c == '4':
#                 color = 'yellow'
#                 rect(offset_x, offset_y, length, color)
#             elif c == '5':
#                 color = '#663300'
#                 rect(offset_x, offset_y, length, color)
#             elif c == '6':
#                 color = 'pink'
#                 rect(offset_x, offset_y, length, color)
#             elif c == '7':
#                 color = '#EEE9BF'
#                 rect(offset_x, offset_y, length, color)
#             elif c == '8':
#                 color = '#87CEFF'
#                 rect(offset_x, offset_y, length, color)
#             print('color', color)
#
#
# # 抽取重复，简化代码
# # 独立功能，拆分逻辑
# def draw_row(x, y, length, row):
#     color_map = {
#         '1': 'black',
#         '2': 'black',
#         '3': 'black',
#         '4': 'black',
#         '5': 'black',
#         '6': 'black',
#         '7': 'black',
#         '8': 'black',
#     }
#     for j, c in enumerate(row):
#         offset_x = x + j * length
#         color = color_map.get(c)
#         print('color', color)
#         if color is not None:
#             rect(offset_x, y, length, color)
#
#
# def draw_char(x, y, a):
#     length = 1
#     for i, row in enumerate(a):
#         offset_y = y - i * length
#         draw_row(x, offset_y, length, row)
#
#
#
#
# # 例子 2
# def max_index(table):
#     lables = table['lables']
#     data = table['data']
#     name_list = [len(lables[0])]
#     sex_list = [len(lables[1])]
#     score_list = [len(lables[2])]
#     note_list = [len(lables[3])]
#     for i in range(len(data)):
#         d = data[i]
#         name_list.append(len(d['name']))
#         sex_list.append(len(d['sex']))
#         score_list.append(len(str(d['score'])))
#         note_list.append(len(d['note']))
#     max_list = [test3.max_list(name_list),
#                 test3.max_list(sex_list),
#                 test3.max_list(score_list),
#                 test3.max_list(note_list)]
#     return max_list
#
# # def max_index(table):
# #     lables = table['lables']
# #     data = table['data']
#
#
# # 过于复杂，这样是不对的
# def str1(n):
#   for i in range(1,9):
#     i = 1
#   while i <= n:
#         i += 1
#         s =  ''.join([str(k) for k in range(i)])
#         print(i -1 ," ", "\t",s[1:len(s) - 1] + ''.join(reversed(s[1:])))
#
# # 约瑟夫环问题
# #        1  2  3  1  2  3  1  2  3  1
# #        2  3     1  2     3  1     2
# #        3        1  2        3     1
# #                 2  3              1
# #                 2                 3
# #                 3
# array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# n = 3
array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
def ytsefu(array, n=3):
    count = 0
    length = len(array)
    # loop 表示当前是数数的第几个人
    loop = 0
    i = -1
    dead = -1
    hsbk = []
    while count < length:
        i += 1
        i %= length
        # 当前数字
        num = array[i]
        if num == dead:
            continue
        else:
            loop += 1
            if loop % n == 0:
                # 发红包
                hsbk.append(num)
                array[i] = dead
                count += 1
    return hsbk

print(ytsefu(array, 3))


def add1(array, i):
    if i != 0 and array[i-1] != 9:
        array[i-1] += 1
    elif i != len(array) - 1 and array[i+1] != 9:
        array[i+1] += 1

def marked_line(array):
    '''
    对于下面这样的 array
    [0, 0, 9, 0, 9]
    标记后是这样
    [0, 1, 9, 2, 9]
    :param array:
    :return:
    '''
    # 切片就是复制 list
    l = array[:]
    for i in range(len(l)):
        n = l[i]
        if n == 9:
            # 左右都加 1
            add1(l, i)
    return l

print(marked_line([0, 0, 9, 9, 0, 9]))



# 增强一致性
# 消除特例
# [
#     [0, 9, 0, 0],
#     [0, 0, 9, 0],
#     [9, 0, 9, 0],
#     [0, 9, 0, 0],
# ]
# [
#     [0, 0, 0, 0, 0, 0],
#     [0, 0, 9, 0, 0, 0],
#     [0, 0, 0, 9, 9, 0],
#     [0, 9, 0, 9, 9, 0],
#     [0, 0, 9, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0],
# ]


# 数字的二进制表示
# 现在的计算机以字节为基本存储单位
# 一个字节 byte 是 8 bit（位）
# 1000 0001
# 1000 0001 1000 0001 1000 0001 1000 0001
print('二进制', 0b1, 0b10, 0b1000)
print('8 进制', 0o1, 0o10, 0o1000)
print('16进制', 0xff, 0x10, 0x1000)


# 排序
#    0  1  2  3  4  5
l = [1, 6, 2, 9, 3, 0]

def index_of_min(array, offset):
    index = offset
    for i in range(offset, len(array)):
        e = array[i]
        if array[index] > e:
            index = i
    return index

def sort(array):
    l = array
    for i in range(len(l)):
        index = index_of_min(l, i)
        l[i], l[index] = l[index], l[i]

sort(l)
print('sort l', l)

# [0, 1, 2, 3, 6, 9]



# 时间空间复杂度
#
# 1，找到一个 list 中 最大的元素
#   n，是数据的规模
#   这个算法的时间复杂度就是 n，术语是 O(n)
# 2，找到一个 list 中 第一个元素
#   1  是时间的花销
#   这个算法的时间复杂度是 1，术语是 O(1)
#   找到一个 list 中 第 1000000000 个元素
#   仍然是 O(1)， 因为它的时间不随着数据的规模增长而增长，是一个常数
# 3，对于一个有序 list，找到一个数字的花费是多少？
#   二分法，专门用于有序列表
#   复杂度是 O(logN)
#   这个 log 不是数学符号，只是一个自己的定义
#   N = 1024  时间是 10
# 4，对于一个 n * n 的矩阵，求和
#   复杂度是 O(n^2)
#
# 时间复杂度实际上是算法的运行时间随着数据规模增长的相关性
#
# 空间复杂度和时间复杂度相似
# 只不过描绘的是算法所占用的空间的增长大小



# 命名
# 变量名取名
#
# 1，临时变量可以用单个字母
# 因为作用域很小，使用频繁，所以可以用单个字母
# for i in list:
# s = students[i]
#
# 2，用词组描绘变量
# number_of_students
# index_of_min
#
# 3，名词用名词描绘
#   函数用动词描绘
#   返回数据的函数用名词描绘
# log()
# draw_line()
# print_student()
# index_of_min()
# length_of_list()
# offset_x
# offset_y
# color_of_pixel()
# random_color()

