# 2016/7/15
#
# ========
# 作业 2
# 注意, 提示在文件最末尾
# ========
#
# 请以之前 3 课的资料和作业作为参考
#
# 请直接在我的代码中更改/添加, 不要新建别的文件


# 导入 log
from utils import log


# 作业 2.1
# 实现函数
# 10 分钟做不出就看提示
def length(s):
    '''
    返回参数 s 的长度, s 是字符串

    :param s: 要计算长度的字符串
    :return: int 类型, 值为参数 s 的长度
    '''

    return len(s)


# 用法
log('长度', length('hello'))


# 长度 5


# 作业 2.2
# 实现函数
# 10分钟做不出来就看提示
def starts_with(s1, s2):
    '''
    s1 是一个字符串
    s2 是一个字符串
    检查 s1 是否以 s2 开头, 返回 True 或者 False

    :param s1: 字符串
    :param s2: 字符串
    :return: bool 类型
    '''
    news = s1[:length(s2)]
    return news == s2


# 用法
log('starts_with', starts_with('guagua', 'gua'))
# starts_with True
log('starts_with', starts_with('guagua', 'melon'))
# starts_with False
log('starts_with', starts_with('melongua', 'gua'))


# starts_with False


# 作业 2.3
# 实现函数
# 10 分钟做不出就看提示
def find_in(s1, s2):
    '''
    s1 是一个字符串
    s2 是一个长度为 1 的字符串
    返回参数 s2 在 s1 中出现的下标
    如果 s2 没有在 s1 中出现, 返回 -1

    :param s1: 字符串
    :param s2: 字符串
    :return: int 类型, 没找到返回 -1, 找到返回下标
    '''

    return s1.find(s2)


# 用法
log('index', find_in('hello', 'h'))
# index 0
log('index', find_in('hello', 'l'))
# index 2
log('index', find_in('hello', 'f'))


# index -1


# 作业 2.4
# 实现函数
# 10 分钟做不出就看提示
def find_all_in(s1, s2):
    '''
    s1 是一个字符串
    s2 是一个长度为 1 的字符串
    返回参数 s2 在 s1 中出现的所有下标组成的 list
    如果 s2 没有在 s1 中出现, 返回 []

    :param s1: 字符串
    :param s2: 字符串
    :return: list 类型, 没找到返回 [], 找到返回包含所有下标的 list
    '''
    result = []
    temp = s1
    for i in range(len(s1)):
        if starts_with(temp, s2):
            result.append(i)
        temp = s1[i + 1:]

    return result


# 用法
log('find all', find_all_in('10121320', '1'))
# find all [0, 2, 4]
log('find all', find_all_in('10121320', '0'))
# find all [1, 7]
log('find all', find_all_in('10121320', '3'))
# find all [5]
log('find all', find_all_in('10121320', '9'))


# find all []


# 作业 2.5
# 实现函数
# 10 分钟做不出就看提示
def find_all_str_in(s1, s2):
    '''
    s1 是一个字符串
    s2 是一个字符串, 长度未知, 不一定为 1
    返回参数 s2 在 s1 中出现的下标组成的 list
    如果 s2 没有在 s1 中出现, 返回 []

    :param s1: 字符串
    :param s2: 字符串
    :return: list 类型, 没找到返回 [], 找到返回由下标组成的 list
    '''

    result = find_all_in(s1, s2)

    return result


# 用法
log('find all str', find_all_str_in('1012100120', '10'))
# find all [0, 4]
log('find all str', find_all_str_in('1012100120', '100'))
# find all [4]
log('find all str', find_all_str_in('1012100120', '3'))


# find all []


# 作业 2.6
# 实现函数
# 10分钟做不出来就看提示
def ends_with(s1, s2):
    '''
    s1 是一个字符串
    s2 是一个字符串
    检查 s1 是否以 s2 结尾, 返回 True 或者 False

    :param s1: 字符串
    :param s2: 字符串
    :return: bool 类型
    '''
    s1newlen = len(s1) - len(s2)
    s1 = s1[s1newlen:]
    return s1 == s2


# 用法
log('ends_with', ends_with('class.py', 'py'))
# starts_with True
log('ends_with', ends_with('gua.txt', 'py'))
# starts_with False
log('ends_with', ends_with('gua.py', 'gua'))
# starts_with False



























# =====
# 提示
# =====
'''
2.1
    for 循环累加


2.2
    for 循环
    或者切片直接比较


2.3
    for 循环, 找到就 return
    否则 return -1


2.4
    for 循环, 找到就 append


2.5
    for 循环, 切片比较, 找到就 append
    切片的语法自行复习之前的资料


2.6
    可以先用之前的函数看看是否包含
    如果包含, 再进一步切片测试是不是在末尾
'''
