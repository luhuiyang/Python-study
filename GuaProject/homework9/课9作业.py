# 2016/7/26
#
# ========
# 作业 (实时更新)
#
# 注意, 作业会在这里实时更新, 有问题请评论
# 注意, 登录论坛后才有评论功能
# ========
# 7/27 更新 9.6
# 7/27 更新 9.1
#
#
# 请直接在我的代码中更改/添加, 不要新建别的文件


# 重新定义我们的 log 函数
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


# 作业 9.1
# 5 分钟做不出就看提示
#
# 本作业基于上次的作业
import classpen

# def click(*args):
#     print('click')
#     print(args)
#     x, y = args
#     length = 50
#     x = (x // length) * length
#     y = (y // length + 1) * length
#     draw_char(x, y, char_8)

# class8 = classpen

selfchar = {
    -1: [
        '00000000000',
        '00001110000',
        '00111111100',
        '00111111100',
        '01111011110',
        '01110001110',
        '01111011110',
        '00111111100',
        '00111111100',
        '00001110000',
        '00000000000',
    ],

}

def draw_label(x, y, text):
    '''
    text 是一个字符串
    以 x y 为左上角坐标画出这个字符串
    字符串中如果存在没有字符图形的字符
    就用一个特殊的字符替代(所以你需要造一个特殊的字符)
    '''
    a = '0123456789'
    result = []
    for i, temp in enumerate(text):
        if not temp in a:
            log('result == ', result)
            result.append(classpen.char.get(-1))
        else:
            log('result == ', result)
            result.append(classpen.char.get(int(temp)))
        log('result == ', result)
    classpen.draw_block_line(x, y, result)


# draw_label(-100, 100, '009i')

char = {
    0: [
        '11111111111',
        '10000000001',
        '10001110001',
        '10010001001',
        '10010001001',
        '10010001001',
        '10010001001',
        '10010001001',
        '10001110001',
        '10000000001',
        '11111111111',
    ],

    1: [
        '11111111111',
        '10000000001',
        '10000100001',
        '10001100001',
        '10000100001',
        '10000100001',
        '10000100001',
        '10000100001',
        '10001110001',
        '10000000001',
        '11111111111',
    ],

    2: [
        '11111111111',
        '10000000001',
        '10011111001',
        '10000001001',
        '10000001001',
        '10011111001',
        '10010000001',
        '10010000001',
        '10011111001',
        '10000000001',
        '11111111111',
    ],

    3: [
        '11111111111',
        '10000000001',
        '10011111001',
        '10000001001',
        '10000001001',
        '10011111001',
        '10000001001',
        '10000001001',
        '10011111001',
        '10000000001',
        '11111111111',
    ],

    4: [
        '11111111111',
        '10000000001',
        '10000010001',
        '10000110001',
        '10001010001',
        '10010010001',
        '10111111101',
        '10000010001'
        '10000010001',
        '10000010001',
        '11111111111',
    ],

    5: [
        '11111111111',
        '10000000001',
        '10011111001',
        '10010000001',
        '10010000001',
        '10011111001',
        '10000001001',
        '10000001001',
        '10011110101',
        '10000000001',
        '11111111111',
    ],

    6: [
        '11111111111',
        '10000000001',
        '10011111001',
        '10010000001',
        '10010000001',
        '10011111001',
        '10010001001',
        '10010001001',
        '10011111001',
        '10000000001',
        '11111111111',
    ],

    7: [
        '11111111111',
        '10000000001',
        '10011111001',
        '10010001001',
        '10000001001',
        '10000001001',
        '10000001001',
        '10000001001',
        '10000001001',
        '10000000001',
        '11111111111',
    ],

    8: [
        '11111111111',
        '10000000001',
        '10011111001',
        '10010001001',
        '10010001001',
        '10011111001',
        '10010001001',
        '10010001001',
        '10011111001',
        '10000000001',
        '11111111111',
    ],

    9: [
        '11111111111',
        '10000100001',
        '10101110101',
        '10011111001',
        '10110111101',
        '11110111111',
        '10111111101',
        '10011111001',
        '10101110101',
        '10000100001',
        '11111111111',
    ],

    -1: [
        '00000000000',
        '00001110000',
        '00111111100',
        '00111111100',
        '01111011110',
        '01110001110',
        '01111011110',
        '00111111100',
        '00111111100',
        '00001110000',
        '00000000000',
    ],

    -2: [
        '00000000000',
        '00110000000',
        '00100000000',
        '00100000000',
        '00100000000',
        '00100000000',
        '00100000000',
        '00100000000',
        '00110000100',
        '00111111100',
        '00000000000',
    ],

    -3: [
        '00000000000',
        '00011111000',
        '00110001100',
        '00100000100',
        '00100000100',
        '00100000100',
        '00100000100',
        '00100000100',
        '00110001100',
        '00011111000',
        '00000000000',
    ],
    -4: [
        '00000000000',
        '00011111100',
        '00110001100',
        '00100000000',
        '00011000000',
        '00000110000',
        '00000001000',
        '00000000100',
        '00110001100',
        '00111111000',
        '00000000000',
    ],

    -5: [
        '00000000000',
        '00111111100',
        '00110000100',
        '00100000000',
        '00100000100',
        '00111111100',
        '00100000100',
        '00100000000',
        '00110000100',
        '00111111100',
        '00000000000',
    ],

    -10: [
        '11111111111',
        '10000000001',
        '10000000001',
        '10000000001',
        '10000000001',
        '10000000001',
        '10000000001',
        '10000000001',
        '10000000001',
        '10000000001',
        '11111111111',
    ],
}


square = [
    [1, 2, 9, 2, 9],
    [1, 9, 2, 2, 2],
    [1, 2, 2, 2, 9],
    [1, 2, 9, 2, 1],
    [9, 2, 1, 1, 0],
]

square_white = [
    [-10, -10, -10, -10, -10],
    [-10, -10, -10, -10, -10],
    [-10, -10, -10, -10, -10],
    [-10, -10, -10, -10, -10],
    [-10, -10, -10, -10, -10],
]



# 作业 9.2
# 无提示
#
# 基于作业 8, 完成完整版的扫雷, 功能如下
# 程序初始状态, 所有格子都是空白
# 用户点击格子后, 检查点击的是什么
# 如果是雷, 则显示所有雷, 并使用 9.1 显示结束语(随便你怎么来)
# 如果是数字或者空白, 则显示这个数字或者空白
# 如果是空白, 不要求像其他扫雷那样显示附近所有空白和数字
def click(*args):
    x, y = args
    log('坐标', x, y)
    a, b = classpen.touched_index(x, y)
    number = square[b][a]
    block = char.get(square[b][a])
    log('字符', block)
    size = 3 * 11
    index_x = a * size - 200
    index_y = 200 - b * size
    classpen.draw_block(index_x, index_y, block)
    if (number == 9):
        line = []
        # for i in range(4):00000000000
        line.append(char.get(-2))
        line.append(char.get(-3))
        line.append(char.get(-4))
        line.append(char.get(-5))
        classpen.draw_block_line(-200, 250, line)
        classpen.draw_mine_map(-200, 200, square)


def saolei():
    classpen.draw_mine_map(-200, 200, square_white)
    classpen.click_method(click)



saolei()


# 作业 9.3
# 5 分钟想不出就看提示
#
# 本作业基于上课的内容
class Node(object):
    def __init__(self, element=0):
        self.element = element
        self.next = None


def contains(node, element):
    '''
    node 是上课的 Node 类
    element 是数字或者字符串, 无所谓
    遍历 node, 判断 element 是否在里面

    :return: bool
    '''
    while node != None:
        log('node.element = ', node.element)
        if element == node.element:
            return True
        else:
            node = node.next
n1 = Node(3)
n3 = Node(5)
n5 = Node(7)
n1.next = n3
n3.next = n5
# log(ensure(contains(n1, 9), '出错啦'),'测试contains')

# 作业 9.4
# 无提示
#
# 本作业基于上课的内容
def node_length(node):
    '''
    node 是上课的 Node 类
    遍历 node, 返回 node 的个数

    :return: int
    '''
    count = 0
    while node != None:
        count += 1
        node = node.next
    return count

ensure(node_length(n1) == 3, 'node_length出错啦')

# 作业 9.5
# 无提示
#
# 本作业基于上课的内容
def last_one(node):
    '''
    node 是上课的 Node 类
    遍历 node, 返回最后一个 node

    :return: node
    '''
    while node.next != None:
        node = node.next
    return node

ensure(last_one(n1) == n5, 'last_one出错啦')


# 作业 9.6
# 看提示做, 做不出也很正常
#
# 本作业基于上课的内容
class Stack(object):
    def __init__(self):
        self.head = Node()

    def push(self, element):
        n = Node()
        n.element = element
        n.next = self.head
        self.head.next = n

    def pop(self):
        n = self.head.next
        self.head.next = n.next
        return n

class Queue(object):
    def __init__(self):
        self.head = Node()

    def enqueue(self, element):
        n = self.head
        while n != None:
            n = n.next
        last = Node()
        n.next = last
        last.element = element

    def dequeue(self):
        n = self.head.next
        self.head.next = n.next
        return n


def parsed_ast(tokens):
    '''
    tokens 是这样的 list
    ['[', '+', 12, '[', '-', 23, 45, ']', ']']

    每一对 [] 都解析为一个元素, 结果解析为这样的 list 并返回
    ['+', 12, ['-', 23, 45]]

    :return: list
    '''
    # stack = Stack()
    temp = []
    for i, item in enumerate(tokens):


        if item == '[':
            # log('temp result = ', result)
            # result.append(parsed_ast(tokens[i + 1:]))
            # break
            temp.append(parsed_ast(tokens[i + 1:]))
            break
        elif item ==']':
            a = parsed_ast(tokens[i + 1:])
            if (temp != []):
                return temp + a
            else :
                return a
        else:
            temp.append(item)


    return temp

def get_result(queue):
    a = Node()
    a = queue.dequeue()




ensure(parsed_ast(['[', '+', 12, '[', '-', 23, 45, ']', ']']) == ['+', 12, ['-', 23, 45]], '最后一题测试')
log('最后一题',parsed_ast(['[', '+', 12, '[', '-', 23, 45, ']', ']']))
log('自己测试',parsed_ast(['[','[','+', '[','*', 11, 22, ']', '[','-', 23, 45,']',']', 3,']']))




classpen.done()
# =====
# 提示
# =====
'''
9.1
draw_label


9.3
contains
    参考上课的 log_nodes


9.6
parsed_ast
    tokens 是这样的 list (本例子有 9 个元素)
    ['[', '+', 12, '[', '-', 23, 45, ']', ']']

    从开始到结束, 把元素 push 入一个 栈 中
    碰到 ']' 元素就从 栈 中 pop 数据直到 pop 的是 '[' 元素
    把这些数据合并成一个 list 并逆序后再 push 入栈
    最终结果是一个只包含一个 list 元素的栈, list 元素如下
    ['+', 12, ['-', 23 45]]
    返回它
    :return: list
'''
