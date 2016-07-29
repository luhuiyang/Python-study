
# 源代码是字符串
'''
[+ 12 34]
'''

# 读取并解析为基本要素
['[', '+', 12, 34, ']']

# 把基本要素解析为 ast（语言的结构化表示）
['+', 12, 34]

# 对 ast 进行解释求值
# apply_all

# 我们的语言成为 ast 后，有两个选择
# 1，解释执行，python/ruby/js
# 2，编译为机器码，然后运行机器码


# [define a 1]
# [log [+ a 2]]
# [log [- 2 3]]
# [define square [n] [* n 2]]



# 课 10
# 今天上课讲 CPU 的运行原理

# 假设我们有这么一个程序
'''
[define a 1]
[define b 2]
[define c [+ a b]]


[if [> a b] a b]
'''
# CPU 的指令
'''
cpu 有指令 还能存储几个数据
存储数据的地方叫做寄存器, 假设有 3 个寄存器
分别用
00010000    a
00020000    b
00030000    c
表示

00000001 load 从内存地址载入一个数据到寄存器
00000010 save 从寄存器往内存地址写入一个数据
00000011 add  把两个寄存器相加，存入第三个寄存器中
00000100 bijc 比较两个寄存器的数据大小，并写入一个结果到标识寄存器中
jump
jump_if_great
jump_if_equal
jump_if_less

# 机器语言
00000001    load
00000000    a 的内存地址 0
00010000    寄存器 a
00000001    load
00000001    b 的内存地址 1
00100000    寄存器 b
00000011    add
00010000    寄存器 a
00100000    寄存器 b
00110000    寄存器 c
00000010    save
00110000    寄存器 c
00000010    c 的内存地址 2

# 汇编语言，就是给指令和寄存器取名字
# 然后用 汇编器 这个程序转化为机器指令
load 0 a
load 1 b
add a b c
save c 2
bijc a b c


# 输入
键盘/鼠标输入

# 输出
屏幕输出

'''

# CPU 如何读取指令并执行
# CPU 指令和程序的对应关系
# 我们如何手写机器语言
# 我们如何把编程语言翻译为机器语言
# (这些知识是计算机行业最初几十年年的成果)
#
#
# 计算机为什么能读懂 1 和 0
# https://www.zhihu.com/question/20112194/answer/32188486
#
#
# 自行搜索下面两个名词
# 冯诺依曼机结构
# 运算器 控制器 CPU
# 存储器
# 输入 输出
#
#
# 图灵机和图灵测试
# 图灵猫



# JSON
# 用文件保存、读取数据


# 数据结构

d = {
    'name': 'gua',
    'height': 169,
}

def test(obj):
    obj['name'] = 'Xiao'


def log(*args):
    print(*args)


print(d)
test(d)
print(d)


class Node(object):
    def __init__(self, element=0):
        self.element = element
        self.next = None

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

n1.next = n2
n2.next = n3

def log_nodes(node):
    while node is not None:
        log('log_nodes', node.element)
        node = node.next

log_nodes(n1)
