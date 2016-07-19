# 2016/07/16
#
# 此为第五课的上课内容
#
# 今天上课的主要内容有
#
# 作业 4 飞速讲解(如果你有不理解的地方, 请提前私下和我提出, 因为这次讲解真的是飞速)
# while 循环
# break 语句
# continue 语句
# dict (字典)
# 读文档 (不在此文件中)
# pass 语句和 ...
# 文件 IO
# 递归
#
# 应该都能看懂, 不懂的稍微做个笔记, 等上课讲解


# 定义我们的 log 函数
def log(*args):
    print(*args)


# ------------
# while 循环
# ------------
#
# while 循环和 for 循环都是循环
# for 适用于循环次数/条件确定的情况, 一般用于遍历一个序列
# while 适用于循环条件/次数不确定的情况
# 详细请看下方资料
#
# 定义一个变量 i
i = 0
# 语法是 while 条件:
# 如果条件成立, 就会一直执行循环体
while i < 5:
    # 函数体, 把 i 打印出来
    log('while 循环 i, ', i)
    # 更改循环条件, 否则就是无限循环了
    # 注意, 这很重要
    i += 1

# 运行, 输出如下
# while 循环 i,  0
# while 循环 i,  1
# while 循环 i,  2
# while 循环 i,  3
# while 循环 i,  4

# 练习
# 用循环输出 5 4 3 2 1, 形式不限


# 更多 while 循环例子
# 使用 while 循环计算 100 内的奇数和
n = 1
sum = 0
while n <= 100:
    if n % 2 == 1:
        sum = sum + n
    n += 1

log('1 到 100 的奇数和是', sum)

# 运行, 输出如下
# 1 到 100 的奇数和是 2500


# break 语句
#
# break 语句可以终止循环
i = 0
while i < 10:
    log('while 中的 break 语句')
    # break 语句执行后, 循环就结束了
    break
    # 因此 i += 1 这一句是不会被执行的
    i += 1

log('break 结束的 i 值', i)
# 运行, 输出如下
# while 中的 break 语句
# break 结束的 i 值 0
#
# 可以看到
# 循环执行了一次就结束了
# i 仍然是 0, 说明 break 后的语句的确没有被执行


# continue 语句
#
# continue 语句可以跳过单次循环
i = 0
while i < 10:
    # 一定要记住改变循环条件, 否则会无线循环
    i += 1
    # 如果 i 是偶数, 则 continue 跳过这次循环
    if i % 2 == 0:
        continue
    log('while 中的 contine 语句', i)

# 运行, 输出如下
# while 中的 contine 语句 1
# while 中的 contine 语句 3
# while 中的 contine 语句 5
# while 中的 contine 语句 7
# while 中的 contine 语句 9
#
# 可以看到
# 只有 1 3 5 7 9 被 log 出来了
# 因为 i 是偶数的时候, 循环体中剩下的部分被跳过了


# ------------
# dict (字典)
# ------------
#
# dict 是一个非常重要的存储数据的类型
# dict 和 list 是最重要的两个存储数据的工具
#
# list 通过数字下标来访问元素
# dict 通过 key(键) 来访问元素
# 详细请看下方资料


# 创建字典
#
taoer = {
    'name': 'gua',
    'height': 169,
}

log('dict ', taoer)

# 运行, 输出如下
# dict  {'name': 'gua', 'height': 169}
#
# 可见, 字典的创建是花括号 {}
# 字典的值是成对出现的, 由冒号分隔开
# 左边的是 key(键), 几乎所有情况下, 都是字符串, 这也是它的主要用途
# 右边的是 value(值), 可以是任意类型, 包括 int str bool list dict 等


# 访问(读取/使用) dict 中的元素
#
# 通过 [] 语法可以用 key 得到 value
log('通过 key 访问 dict 的元素')
log(taoer['name'])
log(taoer['height'])

# 运行, 输出如下
# 通过 key 访问 dict 的元素
# gua
# 169


# 访问不存在的 key 会出错
# taoer 字典中并没有 'age' 这个 key, 因此下面的语句会出错并中断程序
# log(taoer['age'])
# 可以用 get 函数安全地访问一个不存在的 key
# 如果 key 不存在, 则返回 None
log('get 函数访问 dict', taoer.get('age'))
# 使用 get 还可以设置默认值
# 默认值就是说, 当 key 不存在的时候, 返回的一个值
# 不设置的话, 默认就返回 None
log('get 默认值', taoer.get('age', 18))

# 运行, 输出如下
# get 函数访问 dict None
# get 默认值 18
#
# 注意, get 函数的第二个参数是当 key 不存在的时候返回的默认值
# 不设置这个参数的话, 默认值是 None


# 增加, 修改 dict 中的元素
#
# 创建一个新的字典来使用
gua = {
    'name': 'xiaogua',
    'height': 169,
}

# 增加一个元素
gua['sex'] = '男'
log('dict 增加', gua)
log('dict 增加', gua['sex'])

# 修改已有的元素
gua['name'] = 'gua'
log('dict 修改', gua)

# 删除元素
gua.pop('sex')
log('dict 删除', gua)

# 运行, 输出如下 (注意, 字典的输出不一定能保证 key 的顺序, 所以你看到的输出和我这个不一定一样)
# dict 增加 {'sex': '男', 'name': 'xiaogua', 'height': 169}
# dict 增加 男
# dict 修改 {'sex': '男', 'name': 'gua', 'height': 169}
# dict 删除 {'name': 'gua', 'height': 169}
#
# 注意看, 增加了一个新的 key 'sex'
# 并且可以访问到它的值
# 同时, 可以看到 'name' 被修改了
# 另外, key 还会被 pop 函数删除


# dict 的额外的其他操作, 将在课后给出具体信息, 这里仅仅列出函数名
#
# keys
# values
# items
# copy
# update
# pop
# len
# del


# ------------
# pass 语句和 ... 语句
# ------------
#
# Python 使用缩进来控制语句的范围
# 有缩进但是没有语句的代码会被认为是错误
# pass 语句是一个空语句, 什么也不干, 仅仅表示占位, 不会有任何副作用
# 所以如果一个缩进没有语句, 就应该填充 pass 语句
def apple():
    pass


# ... 语句
# ... 语句和 pass 非常相似, 也可以用来表示省略
# 注意, 这是一个只有 Python3 中才有的新功能
def pie():
    ...


# ------------
# 文件 IO
# ------------
#
# 文件 IO 的意思是, 文件的 Input(输入) 和 Output(输出)
# Python 可以方便地读写文件
# 具体请看如下资料


# 打开文件并写入
#
# 这是一个套路, 不要去想过多为什么
# open 是打开文件的函数, 文件首先要被打开, 才能进行读写操作
# open 函数接受 2 个参数
# 第一个是文件的路径, 我们只给出文件名, 那么就是在当前目录下打开这个文件
# 第二个是文件的打开模式, 这里我们用 'w' 表示是要写入内容到这个文件 ('w' 是 write 的意思)
# 通过模块的学习, 大家应该知道 as 用来改名字, 在这里是给打开的文件取个名字
# 所以 f 可以是任意合法的变量名, 一般我们用 f, 比较简单方便
with open('class5.test.txt', 'w') as f:
    # 写入内容到文件
    f.write('greetings from gua')

# 注意观察, 执行过代码后, 应该会在当前目录下生成一个名为 class5.test.txt 的文件
# 打开看看里面的内容, 是 greetings from gua
# 说明我们的确是写入了内容到这个文件中


# 打开文件并读取
#
# 这是一个套路, 不要去想过多为什么, 和上面一样
# 文件的打开模式, 这里变成了 'r' 表示是要从这个文件中读取内容 ('r' 是 read 的意思)
with open('class5.test.txt', 'r') as f:
    # 用 f.read() 读取文件所有内容并赋值给变量 content
    content = f.read()
    log('文件读取', content)

# 运行, 输出如下
# 文件读取 greetings from gua
#
# 注意看, 输出了我们刚刚对文件写入的内容


# ------------
# 递归
# ------------
#
# 递归简而言之就是一个函数调用本身或者两个函数相互调用
# 我们只讨论第一种情况
# 需要注意的是, 递归是一个比较难以理解的概念
# 看不懂, 不理解, 太正常了
# 这需要时间来, 不要急着出斧头强行非要搞懂


# 注意, 接下来的例子都只是例子而已, 实际不会这么写代码
# 递归有适用的场景, 但不会用来求阶乘这样的事情, 只是为了简化描述才用了这个例子
#
# 用递归求阶乘
#
# 阶乘的定义如下
# !n = n * !(n-1)
# 当 n 等于 0 的时候, 阶乘为 1 (不要问为什么, 这是规定)
# 所以可以用递归编写下面的代码
def fac(n):
    # 如果 n 是 0 则返回 1
    # 这是递归终止的条件, 必须要有, 否则无限递归了
    if n == 0:
        return 1
    else:
        # 如果 n 不为 0, 返回 n * fac(n-1)
        # 这时候 n 是已知的, fac(n-1) 需要计算
        # 于是代码进入下一重世界开始计算
        return n * fac(n-1)

log('递归阶乘', fac(5))

# 运行, 输出如下
# 递归阶乘 120


# 用递归求斐波那契数
#
# 斐波那契的定义如下
# fib(n) = fib(n-2) + fib(n-1)
# 当 n 等于 1 2 的时候, fib(n) 为 1
# 所以可以用递归编写下面的代码
def fib(n):
    # 如果 n 是 1 或者 2 则返回 1 作为结果
    # 这是递归终止的条件, 必须要有, 否则无限递归了
    if n == 1 or n == 2:
        return 1
    else:
        # 如果 n 不为 1 和 2, 返回 fib(n-2) + fib(n-1)
        # 这时候 fib(n-2) fib(n-1) 需要计算
        # 于是代码进入下一重世界开始计算
        return fib(n-2) + fib(n-1)

log('递归 fib', fib(6))
log('递归 fib', fib(7))

# 运行, 输出如下
# 递归 fib 8
# 递归 fib 13
