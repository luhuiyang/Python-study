# docstring 和 help
#
#
# import 就是导入一个已经写好了的模块
# 模块就是别人写好的函数 功能的集合
# 从哪里导入呢？
# 导入的优先级分别是
# 1，当前目录
# 2，系统默认的文件夹
# 那么默认文件夹在哪里呢？不用关心

# 我们可以自己写一个模块并导入
# 导入模块不用加上 .py 后缀

import math
import turtle


# 在函数的开头的多行字符串叫做 docstring
# doc 是文档的意思
# 这个东西可以用 help 函数显示出来
def abs(n):
    '''
    这是函数的帮助
    :type n: int
    :rtype: int
    :param n: 这是一个数字，函数返回它的绝对值
    :return: 参数的绝对值
    '''
    if n < 0:
        n = -n
    return n

# help(abs)
# abs('kalsdjf')

# print(abs(-10))

def main():
    help(abs)

# 标准的代码结构
# 整个程序只有这一个入口
# 如果你直接执行代码 __name__ 的值就是 '__main__'
# 如果你被当做模块导入， __name__ 的值就不是 '__main__'
if __name__ == '__main__':
    main()

# print(__name__)
