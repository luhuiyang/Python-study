# 2016/7/17
#
# ========
# 作业 1
# str 花式操作函数
#
# 用到的知识主要是
# 0, 用下标引用字符串
# 1, 字符串切片
# 2, 循环
# 3, 选择 (也就是 if)
#
# 注意, 提示在文件最末尾
# ========
#
# 请以之前 str 相关的内容作为参考
#
# 请直接在我的代码中更改/添加, 不要新建别的文件


# 定义我们的 log 函数
def log(*args):
    print(*args)


# ====
# 测试
# 本次作业起, 我们开始使用自动测试的方法来验证结果
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


# 例子
# 测试的使用
#
# 注意看, 我们使用了上文定义的 ensure 来进行测试
def test_sample():
    # ensure 函数接受两个参数
    # 第一个是一个 bool 值, 如果为 True 则不会有任何反应
    # 否则会打印第二个参数
    ensure(1 == 1, '如果测试失败, 这句话会被打印出来')
    ensure(1 > 2, '测试 1 > 2 失败')


test_sample()


# 调用上面的 test_sample 可以得到如下输出
# *** 测试失败: 测试 1 > 2 失败


# ====
# 资料
# ====
#
# str 函数可以把数字转成字符串
# 例如 str(1) 就能得到 '1'
#


# 作业 1.1
# 10 分钟做不出就看提示
#
def zfill(n, width):
    '''
    n 是 int 类型
    width 是 int 类型

    把 n 的位数变成 width 这么长，并在右对齐，不足部分用 0 补足并返回
    具体请看测试

    :return: str 类型
    '''
    nlen = len(str(n))
    result = str(n)
    # widthlen = len(str(width))
    if nlen < width:
        result = "0" * (width - nlen) + result
        log(result)
    return result


# 测试函数
def test_zfill():
    ensure(zfill(1, 4) == '0001', 'zfill 测试 1')
    ensure(zfill(23, 4) == '0023', 'zfill 测试 2')
    ensure(zfill(12345, 4) == '12345', 'zfill 测试 3')
    ensure(zfill(169, 5) == '00169', 'zfill 测试 4')


# 调用测试函数
# test_zfill()


# 作业 1.2
# 10 分钟做不出就看提示
#
def ljust(s, width, fillchar=' '):
    '''
    s 是 str
    width 是 int
    fillchar 是 长度为 1 的字符串, 默认为空格 ' '

    如果 s 长度小于 width, 则在末尾用 fillchar 填充并返回
    否则, 原样返回, 不做额外处理

    :return: str 类型
    '''
    result = s
    if len(s) < width:
        result += fillchar * (width - len(s))
        log('ljust', result)
    return result


# 测试函数
def test_ljust():
    ensure(ljust('gua', 5) == 'gua  ', 'ljust 测试 1')
    ensure(ljust('guagua', 5) == 'guagua', 'ljust 测试 2')
    ensure(ljust('gua', 5, '*') == 'gua**', 'ljust 测试 3')


# test_ljust()


# 作业 1.3
# 10 分钟做不出就看提示
#
def rjust(s, width, fillchar=' '):
    '''
    s 是 str
    width 是 int
    fillchar 是 长度为 1 的字符串, 默认为空格 ' '

    如果 s 长度小于 width, 则在开头用 fillchar 填充并返回

    :return: str 类型
    '''
    result = s
    if len(s) < width:
        result = fillchar * (width - len(s)) + result
        log('rjust', result)
    return result


# 测试函数
def test_rjust():
    ensure(rjust('gua', 5) == '  gua', 'rjust 测试 1')
    ensure(rjust('guagua', 5) == 'guagua', 'rjust 测试 2')
    ensure(rjust('gua', 5, '*') == '**gua', 'rjust 测试 3')


# test_rjust()


# 作业 1.4
# 10 分钟做不出就看提示
#
def center(s, width, fillchar=' '):
    '''
    s 是 str
    width 是 int
    fillchar 是 长度为 1 的字符串, 默认为空格 ' '

    如果 s 长度小于 width, 则在两边用 fillchar 填充并返回
    如果 len(s) 和 width 互为奇偶, 则无法平均分配两边的 fillchar
    这种情况下, 让左边的 fillchar 数量小于右边

    :return: str 类型
    '''
    result = s
    if len(s) < width:
        log('width = ', width)
        left = int((width - len(s)) / 2)
        right = (width - len(s)) - left
        result = fillchar * left + result + fillchar * right
        log('center', result)
    return result


# 测试函数
def test_center():
    ensure(center('gua', 5) == ' gua ', 'center 测试 1')
    ensure(center('gua', 5, '*') == '*gua*', 'center 测试 2')
    ensure(center('gw', 5) == ' gw  ', 'center 测试 3')
    ensure(center('gua', 6) == ' gua  ', 'center 测试 4')


# test_center()


# 作业 1.5
# 10 分钟做不出就看提示
#
def is_space(s):
    '''
    检查 s 中是否只包含空格

    :param s: 字符串参数
    :return: bool, 如果 s 中包含的只有空格则返回 True, 否则返回 False
    '''
    confirm = " " * len(s)
    log('is_space ', s)
    return confirm == s and len(confirm) > 0


# 测试函数
def test_is_space():
    ensure(is_space(' '), 'center 测试 1')
    ensure(is_space('   '), 'center 测试 2')
    ensure(not is_space(''), 'center 测试 3')
    ensure(not is_space('gua'), 'center 测试 4')


# test_is_space()

# 作业 1.6
# 10 分钟做不出就看提示
#
def is_digit(s):
    '''
    检查 s 中是否只包含数字

    :param s: 字符串参数
    :return: bool, 如果 s 中包含的只有数字则返回 True, 否则返回 False
    '''
    numbers = '01234567890'
    log("is_digit", s)
    for i in s:
        if numbers.find(i) == -1:
            return False
    return True


# 测试函数
def test_is_digit():
    ensure(is_digit('123'), 'is_digit 测试 1')
    ensure(is_digit('0'), 'is_digit 测试 2')
    ensure(not is_digit('  '), 'is_digit 测试 3')
    ensure(not is_digit('1.1'), 'is_digit 测试 4')
    ensure(not is_digit('gua'), 'is_digit 测试 5')


# test_is_digit()


# 作业 1.7
# 10 分钟做不出就看提示
#
def strip_left(s):
    '''
    返回一个「删除了字符串开始的所有空格」的字符串

    :param s: 字符串
    :return:
    '''
    result = ''
    for i in range(len(s)):
        log('i = ', i)
        if s[i] != ' ':
            result = s[i:]
            log('result = ', result)
            return result
    return result


# 测试函数
def test_strip_left():
    ensure(strip_left('  gua') == 'gua', 'strip_left 测试 1')
    ensure(strip_left(' gua  ') == 'gua  ', 'strip_left 测试 2')
    ensure(strip_left('') == '', 'strip_left 测试 3')
    ensure(strip_left('    ') == '', 'strip_left 测试 4')


# test_strip_left()


# 作业 1.8
# 10 分钟做不出就看提示
#
def strip_right(s):
    '''
    返回一个「删除了字符串末尾的所有空格」的字符串

    :param s:
    :return:
    '''
    result = ''
    for i in range(len(s)):
        log('i = ', i)
        index = len(s) - i - 1
        log('index = ', index)
        if s[index] != ' ':
            result = s[:index + 1]
            log('result = ', result)
            return result
    return result


# 测试函数
def test_strip_right():
    ensure(strip_right('  gua') == '  gua', 'strip_right 测试 1')
    ensure(strip_right(' gua  ') == ' gua', 'strip_right 测试 2')
    ensure(strip_right('') == '', 'strip_right 测试 3')
    ensure(strip_right('    ') == '', 'strip_right 测试 4')


# test_strip_right()


# 作业 1.9
# 10 分钟做不出就看提示
#
def strip(s):
    '''
    返回一个「删除了字符串首尾的所有空格」的字符串

    :param s:
    :return:
    '''
    right = strip_left(s)
    return strip_right(right)


# 测试函数
def test_strip():
    ensure(strip('  gua') == 'gua', 'strip 测试 1')
    ensure(strip(' gua  ') == 'gua', 'strip 测试 2')
    ensure(strip('') == '', 'strip 测试 3')
    ensure(strip('    ') == '', 'strip 测试 4')

# test_strip()


# 作业 1.10
# 10 分钟做不出就看提示
#
def replace(s, old, new):
    '''
    3 个参数 s old new 都是字符串
    返回一个「将 s 中的 old 字符串替换为 new 字符串」的字符串
    假设 old 存在并且只出现一次
    :return:
    '''
    newhead = s.find(old)
    if newhead != -1:
        oldlen = len(old)
        result = s[:newhead] + new + s[newhead + oldlen :]
        log('raplace result = ', result)
        return result
    return s


# 测试函数
def test_replace():
    ensure(replace('hello, world', 'world', 'gua') == 'hello, gua', 'replace 测试 1')
    ensure(replace('hello', 'world', 'gua') == 'hello', 'replace 测试 2')
    ensure(replace('hello', 'll', 'gua') == 'heguao', 'replace 测试 3')

test_replace()


# =====
# 提示
# =====
'''
1.1
zfill
    字符串拼接


1.2
ljust
    字符串拼接


1.3
rjust
    字符串拼接


1.4
center
    算好头尾再拼接


1.5
is_space
    循环检测


1.6
is_digit
    预定义数字
    再循环检测


1.7
strip_left
    循环查找到第一个不为空格的字符的下标然后切片返回


1.8
strip_left
    和 1.7 类似, 注意好切片的下标


1.9
strip
    利用 1.7 1.8


1.10
replace
    查找切片 2 次再拼接
'''
