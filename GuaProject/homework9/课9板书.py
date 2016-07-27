# 数据结构
# 表、链表
# 栈
# 队列

def log(*args):
    print(*args)

# 栈的三个基本操作
# push pop top
def push(stack, element):
    stack.append(element)

def pop(stack):
    e = stack[-1]
    del stack[-1]
    return e

def top(stack):
    return stack[-1]

# push_all 是我们扩展的栈操作
def push_all(stack, *args):
    for e in args:
        stack.append(e)

# 测试使用
l = []
# push(l, 1)
# push(l, 2)
# push(l, 3)
push_all(l, 1, 2, 3)
log(pop(l))
log(pop(l))
log(pop(l))


# 队列的 2 个操作
# enqueue 入队
# dequeue 出队

def new_queue():
    return []

def enqueue(queue, element):
    queue.append(element)

def dequeue(queue):
    e = queue[0]
    del queue[0]
    return e

q = new_queue()
enqueue(q, 1)
enqueue(q, 2)
enqueue(q, 3)
log('队列测试')
log(dequeue(q))
log(dequeue(q))
log(dequeue(q))


# 面向对象的 栈 和 队列
#
# Stack 类
# 这就是封装，只关心使用方法，不关心实现细节
class Stack(object):
    def __init__(self):
        self.array = []
        # 设置一个容量
        self.capacity = 3
        self.number_of_elements = 0

    def push(self, element):
        if self.number_of_elements < self.capacity:
            self.number_of_elements += 1
            self.array.append(element)
        else:
            print('栈溢出了')

    def pop(self):
        if self.number_of_elements > 0:
            self.number_of_elements -= 1
            stack = self.array
            e = stack[-1]
            del stack[-1]
            return e
        else:
            log('empty stack')

s = Stack()
s.push('you')
s.push('are')
s.push('how')
s.push('1111')
log(s.pop())
log(s.pop())
log(s.pop())
log(s.pop())

# Queue 类
class Queue(object):
    def enqueue(self, element):
        ...

    def dequeue(self):
        ...


# 传统方式实现的 Stack 和 Queue
class ClassicStack(object):
    def __init__(self):
        self.head = Node()

    def push(self, element):
        # 插入栈顶，让 head.next 为栈顶
        n = Node(element)
        # n.element = element
        n.next = self.head.next
        self.head.next = n

    def pop(self):
        n = self.head.next
        self.head.next = n.next
        return n.element

class Node(object):
    def __init__(self, element=0):
        self.element = element
        self.next = None

s1 = ClassicStack()
s1.push('hello')
s1.push('python')
log(s1.pop())
log(s1.pop())

n1 = Node()
n2 = Node()
n3 = Node()
n4 = Node()
n5 = Node()

n1.element = 1
n2.element = 2
n3.element = 3
n4.element = 4
n5.element = 5

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

def log_nodes(node):
    while node is not None:
        log('log_nodes', node.element)
        node = node.next

log_nodes(n1)


# 链表
class LinkedList(object):
    ...



# 解释器
# 最初的作业，能够求下面的值
['+', 1, 2, 3, 4]
# 如果每一个元素都是一个表达式而不是 1 2 3 这样的数值呢？
# 用 type 判断类型，递归调用自身求值
# 这个东西就叫做 树（ast，abstract syntax tree，抽象语法树）
['+', 1, ['-', 2, 3]]

# 为了得到 ast，就要解析一个 list（符号列表）
# 这个过程，叫做 语法分析，parse
# 我们有一个这样的输入
['[', '+', 12, '[', '-', 23, 45, ']', ']']
# 解析为 这样的 ast
['+', 12, ['-', 23, 45]]

def parser(array):
    ...

# 为了得到一个符号列表
['[', '+', 12, '[', '-', 23, 45, ']', ']']
# 就要解析下面这样的字符串
'''
[+ 12 [- 23 45]]
'''
# 这个过程术语叫做 词法分析
# lexer, tokenizer
#
# 为了解析这样的字符串
# 就要定义基本的符号要素
# []
# +-*/
# 数字

# 从源代码直接到执行结果这样的过程，叫做解释执行
# 还有一种是生成可执行文件（在windows上通常是 exe 格式）然后运行
# 这种叫做编译执行

# 解释器直接得到结果
# 编译器会生成可执行文件然后用户去执行生成的文件得到运行结果

# CPU 如何执行指令
# 只能认数字
# 不同的数字代表了不同的功能
# 1010 1010 1010 1011
# 0010 1010 1010 1011
# 1010 代表 +
# 0010 代表 -
# 记忆数字太麻烦
# 于是发明了汇编语言
# 汇编语言是给指令取了一个名字
# 比如 add 代表 1010
# 比如 sub 代表 0010
# 实际上就是用英语替代机器码
