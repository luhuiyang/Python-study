# 2016/7/19
#
# ========
# 作业 1
#
#
# 注意, 提示在文件最末尾
# ========
#
#
# 请直接在我的代码中更改/添加, 不要新建别的文件


# 又一次重新定义我们的 log 函数
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


# ====
# 资料
# ====
#
# str 函数可以把数字转成字符串
# 例如 str(1) 就能得到 '1'
#


# 作业 1.1
# 11 分钟做不出就看提示
#
def join(delimiter, array):
    '''
    delimiter 是 str
    array 是包含 str 的 list

    把 array 中的元素用 delimiter 连接成一个字符串并返回
    具体请看测试

    :return: str
    '''
    result = ''
    delimiter = str(delimiter)
    right = len(delimiter)
    for n in array:
        result += n + delimiter
        log('join', result[:-right])
    return result[:-right]


# 测试函数
def test_join():
    ensure(join('#', ['hello', 'gua']) == 'hello#gua', 'join 测试 1')
    ensure(join(' ', ['hello', 'gua']) == 'hello gua', 'join 测试 2')
    ensure(join('\n', ['multi', 'line', 'string']) == 'multi\nline\nstring', 'join 测试 3')
    # ensure(join(169, 5) == '00169', 'join 测试 4')


# test_join()


# 作业 1.2
# 12 分钟做不出就看提示
#
def split(s, delimiter=' '):
    '''
    s 是 str
    delimiter 是 str, 默认为空格 ' '

    以 delimiter 为分隔符号, 返回一个 list
    具体请看测试

    :return: list
    '''
    results = []
    temp = ''
    for n in s:
        if n != delimiter:
            temp += n
        else:
            results.append(temp)
            temp = ''
    results.append(temp)
    log('split ', results)
    return results


# 测试函数
def test_split():
    ensure(split('1 2 3') == ['1', '2', '3'], 'split 测试 1')
    ensure(split('a,b,c', ',') == ['a', 'b', 'c'], 'split 测试 2')
    ensure(split('a=b&c=d', '&') == ['a=b', 'c=d'], 'split 测试 3')


# test_split()


# 作业 1.3
# 10 分钟做不出就看提示
#
def replace_all(s, old, new):
    '''
    s old new 都是 str
    返回一个「将 s 中出现的所有 old 字符串替换为 new 字符串」的字符串

    :return: str 类型
    '''
    pass


# 测试函数
def test_replace_all():
    ensure(replace_all('hello, world', 'o', '*') == 'hell*, w*rld', 'replace_all 测试 1')
    ensure(replace_all('a#b#c#d', '#', ' ') == 'a b c d', 'replace_all 测试 2')


# 作业 1.4
# 10 分钟做不出就看提示
#
def str1(n):
    '''
    n 是 int
    返回这样规律的字符串
    n       返回值
    1       '1'
    2       '121'
    3       '12321'

    :return: str
    '''
    left = ''
    right = ''
    for i in range(1, n):
        left += str(i)
        right = str(i) + right
        log('left ', left, ' right ', right)
    log('str1 result = ', left + str(n) + right)
    return left + str(n) + right


# 测试函数
def test_str1():
    ensure(str1(1) == '1', 'str1 测试 1')
    ensure(str1(3) == '12321', 'str1 测试 2')
    ensure(str1(4) == '1234321', 'str1 测试 3')


# test_str1()

# 作业 1.5
# 10 分钟做不出就看提示
#
def str2(n):
    '''
    n 是 int
    返回这样规律的字符串
    n       返回值
    1       'A'
    2       'ABA'
    3       'ABCBA'

    :return: str
    '''
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    left = ''
    right = ''
    for i in range(n - 1):
        left += upper[i]
        right = upper[i] + right
        log('left ', left, ' right ', right)
    log('str1 result = ', left + upper[n - 1] + right)
    return left + upper[n - 1] + right


# 测试函数
def test_str2():
    ensure(str2(1) == 'A', 'str1 测试 1')
    ensure(str2(3) == 'ABCBA', 'str1 测试 2')
    ensure(str2(4) == 'ABCDCBA', 'str1 测试 3')


test_str2()


# 作业 1.6
# 10 分钟做不出就看提示
#
def add_table():
    '''
    返回这样格式的加法口诀表(没写全, 但是要返回完整的)
    [
        '1 + 1 = 2',
        '2 + 1 = 3  2 + 2 = 4',
        '3 + 1 = 4  3 + 2 = 5  3 + 3 = 6',
    ]

    :return: str
    '''



# =====
# 提示
# =====
'''
1.1
join
    循环字符串拼接


1.2
split
    找下标切片


1.3
replace_all
    使用上面两个函数


1.4
str1
    str() 函数


1.5
str2
    预先存储所有的大写字母


1.6
add_table
    使用一个辅助函数生成单行 list 再使用上面的 join
'''
