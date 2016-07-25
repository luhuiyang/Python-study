# 2016/07/21
#
# 此为第七课的上课内容
#
# 今天上课的主要内容有
#
# 作业 6 的部分答案
# **kwargs  关键字参数
# 类 与 面向对象
# 魔法方法 和 魔法属性
#
# 应该能看懂一部分, 不懂的稍微做个笔记, 等上课讲解(也可以
# 提前在群/私聊问我)


# 又一次定义我们的 log 函数
def log(*args):
    print(*args)


# =====
# **kwargs  关键字参数
# =====
#
# 在 Python 中, 即使一个参数没有默认值, 也可以在调用时用
# 参数名指定参数(见例子)
def gua(name, sex, height=169.0):
    print(name, sex, height)

gua('gua', 'male')
gua('gua', 'male', 1.69)
gua(height=1.69, name='gua', sex='male')

# 输出如下
# gua male 169.0
# gua male 1.69
# gua male 1.69

# 上节课讲过使用 * 表示多参数
# 本次要讲的是 ** 关键字参数
# 和 *args 类似, 可以自行脑补测试一下
# 一般叫 **kwargs, 是 key word arguments 的缩写
# 对于上面的例子, 用 关键字参数 的方法如下
info = {
    'name': 'Gua',
    'sex': 'Male',
    'height': 169.9,
    'note': 'very gua',
}

def gua1(**kwargs):
    log('gua 1 called', kwargs)

gua1(**info)
gua1(name=1, age=2, weight=3)
# 输出如下
# Gua Male 169.9
#


#
# =====
# 类 与 面向对象
# =====
#
# 语言自带的数据类型有限, 要表示复杂的数据, 必须有复杂的数据类型
# 我们可以用字典表示复杂类型, 比如作业 6.2 中的 student 字典
# 它表示了一条学生信息
#
# 类, 就是语言提供的自定义数据类型的机制
# 它可以比字典更方便地表示复杂类型, 并能实现更多功能
# 例子如下
#

# class 是用来声明 类 的特殊语法
# Student 是类名, 一般首字母大写(驼峰命名法(搜))
# 括号中的 object 是继承的父类, object 是最基础的类
# 类 中双下划线的 函数 和 变量 叫 魔法函数/魔法变量(稍后会讲)
# 先看如何使用再看定义方法
class Student(object):
    # 定义一个函数, 类的函数叫 方法 (单纯只是名字不同)
    # __init__ 是一个特殊的名字
    # 第一个参数叫 self, 你可以随意取名, 但强烈建议使
    # 用 self (一致性)
    def __init__(self):
        log('初始化的时候会调用这个函数')
        # 用 self.变量名 来创造一个只有类才能访问的变量
        self.name = 'gua'
        self.height = 169

# 对 类 调用得到一个「类的实例」
# 赋值给变量 s1
# 这时候 s1 引用的是一个 Student 类型(也就是对象 Student 的实例)
# 也称之为 对象
s1 = Student()

# 可以通过 . 语法访问对象的属性(也就是 __init__ 函数中
# 用 self.变量名 创造的变量)
# 类的变量叫做 属性(单纯只是名字不同)
log('class, s1', s1.name, s1.height)
# 输出如下
# class, s1 gua 169

# ==
# 可以改变 s1 的属性
s1.name = 'xiaogua'
s1.height = 1.69

log('class, s1 属性', s1.name, s1.height)
# 输出如下
# class, s1 属性 xiaogua 1.69

# ==
# 可以创建多个互相独立的实例
s2 = Student()
s3 = Student()
s2.name = 'gua II'
s3.name = '三代瓜'
log(s2.name, s3.name)

# =
# 可以给类增加一些方法(函数)
class StudentInfo(object):
    def __init__(self):
        self.name = ''
        self.height = 0

    def show(self):
        log('student info', self.name, self.height)

    def update(self, name, height):
        self.name = name
        self.height = height

# 初始化
info = StudentInfo()
# 调用 info 的 show 方法
# 注意, show 的第一个参数 self 是不用传递的
# Python 自动帮你处理第一个参数
# 实际上相当于 StudentInfo.show(info)
# info.show()
# 调用 info 的 update 方法
# 也是不用传递 self 的
info.update('xiao', 169.98)
info.show()

# =
# 封装, 上面 show 和 update 就是封装的例子
# 意思是说把一些操作做好, 对外部来说只需要简单调用即可
#

# =
# 继承
# 继承是说, 父类的东西你可以直接拿来用
class Phone(object):
    def __init__(self):
        self.price = 0

    def power_off(self):
        log('关机, 手机')

    def power_on(self):
        log('开机, 手机')


class AnVo(Phone):
    def power_on(self):
        log('安卓, 开机')

# 初始化并调用
p = Phone()
p.power_on()
p.power_off()

a = AnVo()
# 因为 AnVo 实现了自己的 power_on 所以这里调用的是自己的
a.power_on()
# power_off 是继承自父类的方法
a.power_off()


# =
# 类主要的优势就是 字典的替代品 和 可封装方法
# 其他上课要讲的杂项
# 组合, 多态(duck type)

def add(a, b):
    return a + b

log('duck type 1', add(1, 2))
log('duck type 2', add('hello', 'gua'))

# ===
# 魔法方法和魔法属性
# ===
class Circle(object):
    def __init__(self, radius):
        self.r = radius

    # 双下划线包围的方法叫做魔法方法
    # __add__ 是一个魔法方法
    # 一些特殊的操作符实际上是调用了这些魔法方法而已(看例子)
    def __add__(self, number):
        return self.r + number

    def show(self):
        log('circle.show, ', self.r)

    # def __str__(self):
    #     return '自定义的 __str__ 方法, r:'.format(self.r)

c = Circle(10)
c.show()
log('circle + ', c + 20)
# c + 20 实际上变成了以下这句
# c.__add__(20)

# 输出如下
# circle.show,  10
# circle +  30

# Python 中 数字什么的也是对象
# 所以下面的表达式中
# 1 + 2
# 相当于
# (1).__add__(2)
log('数字也是对象 ',
    (1).__add__(2),
    (10).__mul__(9),
    10 * 9
    )
# 双下划线包围的属性叫做魔法属性
log('魔法属性', c.__class__.__name__)

log((1).__str__(), [1, 2].__str__(), [3, 4])
log(str([1, 2, 4]), [1, 2, 4].__str__())
log(str(c), c.__str__())

def str(obj):
    return obj.__str__()

#
# 魔法方法有很多, 这里不一一列举了, 给出资料即可
# 也就是说, Python 中的操作符实际上是一些特殊的函数
# 想知道具体的话, 可以参考下面的链接(想看的话随便看看即可, 来日方长)
# http://pyzh.readthedocs.io/en/latest/python-magic-methods-guide.html#id1


# ===
# 上课要讲的其他杂项
# ===
#
# 可以使用 del 删除变量或删除数组中的元素
l = ['hello', 'gua', 'evening']
del l[1]
log('del', l)

people = {
    'name': 'gua',
    'sex': 'male',
}
log('del dict', people)
del people['sex']
log('del dict', people)

# del 还可以删除变量
name = 'gua'
log('name, ', name)
del name
# 已经被删除了变量，不能引用了
# log(name)

# 全局变量不能修改
name = 'xiao'
def update1():
    # log('update 1', name)
    # 可以引用，但是不能赋值
    name = 'Gua'

update1()
log('更新后', name)

# 交换变量的值 a, b = b, a
a = 1
b = 2
print('a, b', a, b)
a, b = b, a
print('交换 ab', a, b)

# 链式比较
grade = 7
if 6 < grade < 9:
    print('初中生')

# if 的时候的类型, 不能用隐式, if '': 这样是不行的 必须明确
word = ''
hidden = True
code = 0
if code != 0:
    print('code 2')
else:
    print('code 1')

if not word:
    print('空字符串 不清洁的写法')


