# 2016/07/19
#
# 此为第六课的上课内容
#
# 今天上课的主要内容有
#
# 作业 5.1 讲解重要的几个思路(其他以答案+注释的形式给出)
# 数据类型
# 多行字符串和转义符号
# 高阶函数
# 匿名函数 lambda
# *args (多参数)
# 列表推倒(导)
# 获取输入 input
#
# 应该都能看懂, 不懂的稍微做个笔记, 等上课讲解(也可以提前在群/私聊问我)


# 再次定义我们的 log 函数
def log(*args):
    print(*args)


# =====
# 数据类型
# =====
#
# 在 Python 中, 每一个变量(也就是每一个值)都有一个类型
# 内置的基本数据有以下几种类型
# int          整数（integer）
# str          字符串
# float        浮点数
# bool         布尔变量（只有两个值True或False）
# None         空数据类型，表示空
#
# 除了基本数据类型外, 还有 list dict 甚至我们自己定义的类型
# 函数也是一个变量, 稍微特殊点, 但在 Python 中没什么本质不同, 它的类型是函数
#
# 为一个变量赋值就创建了一个变量
# Python 中, 变量只是对值的一个引用
# 比如下面, 分别把 3 个不同类型的值赋值给变量 a
a = 1       # a 是 int
a = 1.1     # 是 float
a = 'good'  # string 类型

# 可以用 type 函数得到一个变量的类型
a = 10
b = 20.0
c = 'I am good'
log('type a', type(a))
log('type b', type(b))
log('type c', type(c))

# 运行, 输出如下
# type a <class 'int'>
# type b <class 'float'>
# type c <class 'str'>


# 浮点数
#
# 带小数点的数叫浮点数（float）
# 看看以下表达式的结果
# 5/2
# 5/2.0
# 5.0/2
#
# 如果只有一个 0, 则可以省略，比如
# 5/.2
# 5/2.
# 但不要这么做，这样不好，有人喜欢这么做，因为没教好


# =====
# 字符串和多行字符串
# =====
#
# 字符串就是一段字符, 用引号引起来的内容(单引号和双引号等价, 但是必须成对出现)
#
# 单引号
# 'string'
#
# 双引号
# "string"
#
# 多行字符串要用三引号，三引号可以是三个单引号也可以是三个双引号，成对出现即可
a = '''多
行
字符串'''

log('多行字符串', a)

a = """
i
am
good
"""

log('多行字符串 2', a)

# 多行字符串可以用作 docstring
# 也可以用作多行注释(你只要不用它 相当于注释了)

# 不同的数据类型是不能混用的
# 比如 float 就不能当下标


# =====
# 转义符
# =====
#
# 在代码中表示字符串的时候, 很多东西不方便表示, 因此我们使用转义符的方式来表示
# 转义符是字符串中的特殊符号，由反斜杠（backslash）开始，接另一个字符结束
# 常用的转义符有
# 还有一些别的转义符，但极少使用，对于这种东西，不必记忆，知道有这么回事就好了。
# \n     # 表示一个换行符
# \t     # 表示一个 TAB（制表符）
# \\     # 表示一个反斜杠 \
# \a     # 表示系统警铃声，有的系统不会响
# \'     # 表示一个单引号
# \"     # 表示一个双引号
#
# 例子：
log('I\'a\tm \n\ngood\n')
#
# 


# =====
# 高阶函数
# =====
#
# 高阶函数这个名字很唬人, 实际上概念很简单——函数可以作为参数传递
#
# 有什么用呢？灵活性高，舒适度佳
# 请看例子
#
# int 函数是用来把数据转换成 int 类型的一个函数
log('int ', int(6.3))

def process(array, processor):
    '''
    array 是一个列表
    processor 是一个函数, 注意, 这是一个函数, 所以可以调用

    把 array 中的每个元素都用 processor 函数处理并返回一个新的 list
    '''
    l = []
    for a in array:
        # processor 必须能调用成功, 否则这里就跪了
        element = processor(a)
        l.append(element)
    return l

# 创建一个 list, 包含 3 个 float
array = [1.1, -2.2, 3.3]

# int str abs 分别是内置函数, 前两个是转换类型的, abs 是用来求绝对值的
int_list = process(array, int)
str_list = process(array, str)
abs_list = process(array, abs)
log('int_list', int_list)
log('str_list', str_list)
log('abs_list', abs_list)

# 输出结果如下
# 我们可以看到, process 函数通过 参数传进来的函数 对数据进行了处理
# int_list [1, -2, 3]
# str_list ['1.1', '-2.2', '3.3']
# abs_list [1.1, 2.2, 3.3]


# =====
# 匿名函数 lambda
# =====
#
# 有时候要传递高阶函数的时候, 函数很短, 可能就一行
# 如果去定义一个新函数有人觉得划不来, 就想了一个偷懒的办法
# 那就是匿名函数
# 匿名函数在 Python 中叫 lambda(一个数学符号)
# 匿名函数的意思是没有函数名, 一般定义了就用

# 例子
# 定义一个 square 函数求平方
def square(n):
    return n * n

# 用上面的 process 函数处理试试
array = [1, 2, 3]
square_list = process(array, square)
log('square_list', square_list)

add1 = lambda n: n + 1
'''
上面这行相当于
def add1(n):
    return n + 1
'''
add_list1 = process(array, add1)
add_list2 = process(array, lambda n: n + 1)
log('add_list1', add_list1)
log('add_list2', add_list2)

# 输出结果如下
# square_list [1, 4, 9]
# add_list [2, 3, 4]

'''
# lambda 定义多参数函数如下
lambda a, b: a + b

# 可以看到 lambda 可以定义一个函数
# 但是 lambda 功能有限, 只能定义单行并且返回数据的函数
# 了解一下即可
'''


# =====
# *args (多参数)
# =====
#
# 在函数有多个参数的时候, 或者接受无限参数的时候, Python 提供便捷的处理流程
def add_all(a, b, c, d, e, f, g):
    '''
    函数接受 7 个 int 参数并且返回 它们的合
    '''
    return a + b + c + d + e + f + g

# 调用方式如下
log('add all', add_all(1, 2, 3, 4, 5, 6 ,7))
# 参数过多, 调用起来很麻烦
# 简便的方式是通过一个 list 装参数然后传给函数
# Python 提供的机制如下
# 给一个 list 加上 * 当参数传递的时候
# 这个 list 会被解开分别传递给函数
arg_list = [1, 2, 3, 4, 5, 6, 7]
log('add all arg_list', add_all(*arg_list))

# 输出如下
# add all 28
# add all arg_list 28

# 还可以这样定义函数, 方便函数的处理
def add_numbers(*args):
    '''
    注意, args 是一个 list
    '''
    s = 0
    for n in args:
        s += n
    return s

# 然后这样调用
log('add numbers', add_numbers(1, 2, 3, 4, 5))
# 或者继续那样调用
numbers = [1, 2, 3, 4, 5, 6]
log('add numbers list', add_numbers(*numbers))


# =====
# 列表推倒(导)
# =====
#
# 在上面的 process 函数中, 我们处理一个 list 并且添加进一个新的 list
#
array = [1, 2, 3, 4, 5]
# 把 array 里面每个元素都加上 100 并生成一个新的 list 的步骤如下
# 先创建一个新的 list
l = []
# 遍历老 list
for n in array:
    # 处理元素后添加进新的 list
    l.append(n + 100)

# 使用列表推倒, 可以简化代码
# 方式如下
numbers = [n + 100 for n in array]

log('+100 list', l)
log('+100 numbers', numbers)

# 输出如下
# +100 list [101, 102, 103, 104, 105]
# +100 numbers [101, 102, 103, 104, 105]

# 使用 if 过滤数据
# 现在只要偶数不要奇数
#
# 老办法如下
l = []
# 遍历老 list
for n in array:
    # 处理元素后添加进新的 list
    if n % 2 == 0:
        l.append(n + 100)

# 使用列表推倒, 可以简化代码
# 方式如下
numbers = [n + 100 for n in array if n % 2 == 0]

log('+100 filter list', l)
log('+100 filter numbers', numbers)

# 输出如下
# +100 filter list [102, 104]
# +100 filter numbers [102, 104]


# =====
# 获取输入 input
# =====
#
# 程序可以在运行时通过终端获取用户输入
# 例子如下

# 注意 input 函数会卡住整个程序, 直到用户在终端输入内容并回车
# input 得到的数据类型是 str
name = input()
log('name', name)
