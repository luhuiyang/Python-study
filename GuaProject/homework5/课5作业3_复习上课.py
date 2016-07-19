# 2016/7/18
#
# ========
# 作业 3
# 复习上课的知识
#
# 用到的知识主要是上课预习的内容
#
# 注意, 提示在文件最末尾
# ========
#
# 请直接在我的代码中更改/添加, 不要新建别的文件


# 定义我们的 log 函数
def log(*args):
    print(*args)


# ====
# 测试
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
# 注意, 没提供测试的题目自行编写测试函数
# ====
#


# 作业 3.1
# 15 分钟做不出就看提示
#
def adds(array, newlen):
    '''
    :param array:  list
    :param newlen:  新的长度
    :return:  按照新的长度，格式化list里面的元素
    '''
    result = []
    for i in array:
        i = '+ ' + i
        i = i + (newlen - len(i) - 1) * ' ' + '+'
        result.append(i)
        log('result ', result)
    return result


def pretty_log(array):
    '''
    array 是 list 类型, 里面的元素都是字符串

    按如下的格式返回这个 array
    假设 array 是 ['python', 'js', 'objective-c']
    那么返回的数据是一个列表, 多了首尾两个元素
    [
        '+++++++++++++++',
        '+ python      +',
        '+ js          +',
        '+ objective-c +',
        '+++++++++++++++',
    ]
    :return: 包含了 str 的 list
    '''
    newlen = 0
    for i in array:
        if len(i) > newlen:
            newlen = len(i)
    newlen += 4;
    result = []
    result.append('+' * newlen)
    result += adds(array, newlen)
    result.append('+' * newlen)
    return result


print(ensure(pretty_log(['python', 'js', 'objective-c']) == [
    '+++++++++++++++',
    '+ python      +',
    '+ js          +',
    '+ objective-c +',
    '+++++++++++++++',
], '1'))


# 作业 3.2
# 15 分钟做不出就看提示
#

def top(students):
    '''
    students 是 list 类型
    里面的每个元素都是如下格式的字典
    {
        'name': 'gua',
        'sex': '男',
        'score': 127,
    }
    返回 score 最高的那个元素(字典)

    :return: 包含最高分学生信息的 字典
    '''
    result = students[0]
    for i in students:
        if i['score'] > result['score']:
            result = i
    log('resultmap', result)
    return result


# 目前只有两个数据, 自行扩充到 5 个
# 自行扩充数据到 5 个
student_list = [
    {
        'name': 'gua',
        'sex': '男',
        'score': 127,
    },
    {
        'name': 'gua',
        'sex': '男',
        'score': 99,
    },
    {
        'name': 'gua',
        'sex': '男',
        'score': 98,
    },
    {
        'name': 'gua',
        'sex': '男',
        'score': 66,
    },
    {
        'name': 'gua',
        'sex': '女',
        'score': 199,
    },
]

ensure(top(student_list) == {
    'name': 'gua',
    'sex': '女',
    'score': 199,
}, '1')


# 作业 3.3
# 10 分钟做不出就看提示
#
def formated_weekday(day):
    '''
    day 是代表星期的数字, 从周一到周日分别是 1 2 3 4 5 6 7
    返回 '星期一' '星期二' 这样的描述字符串

    :return: str 类型
    '''
    temp = str(day)
    numbers = '1234567'
    days = '一二三四五六日'
    index = numbers.find(temp)
    if index != -1:
        log('result weedkay = ', '星期' + days[index])
        return '星期' + days[index]
    return None


ensure(formated_weekday(7) == '星期日', '1')


# 作业 3.4
# 10 分钟做不出就看提示
#
def discount(price, grade=None):
    '''
    price 是一个 int
    grade 一共 6 种取值, 默认为 None, 其他如下
        '小学生'
        '初中生'
        '高中生'
        '大学生'
        '研究生'
    对应的折扣分别是 5 6 7 8 9
    如果调用者没有给出 grade 参数, 也就是 grade 为 None 的话, 没有折扣

    :return: 折扣后的价格
    '''
    grades = {
        '小学生': 5,
        '初中生': 6,
        '高中生': 7,
        '大学生': 8,
        '研究生': 9,
    }
    if None == grade:
        return price
    result = price * grades[grade] / 10
    log(grade, ' count ', grades[grade])
    log(grade, ' ', result)
    return result


# 测试函数
def test_discount():
    ensure(discount(100, '小学生') == 50, 'discount 测试 1')
    ensure(discount(200) == 200, 'discount 测试 2')
    ensure(discount(300, '研究生') == 270, 'discount 测试 3')


# test_discount()


# 作业 3.5
# 10 分钟做不出就看提示
#
def index_of_max(array):
    '''
    array 是一个 list, 里面的每个元素都是 int
    返回最大值对应的下标

    :return: int
    '''
    temp = array[0]
    result = 0
    for index, i in enumerate(array):
        log('i = ', i, ' index = ', index, ' temp = ', temp)
        if temp < i:
            temp = i
            result = index
    return result


# 测试函数
def test_index_of_max():
    ensure(index_of_max([0, 1, 3, 2, ]) == 2, 'index_of_max 测试 1')
    ensure(index_of_max([4, 3, 2, 1, ]) == 0, 'index_of_max 测试 2')
    ensure(index_of_max([1]) == 0, 'index_of_max 测试 3')


test_index_of_max()


# 注意
#
# 下面的作业需要 课3作业2 的内容, 复制如下
#
# 注意 下面几题中的参数 op 是 operator(操作符) 的缩写
#
# 作业 11
# 实现 apply 函数
# 参数如下
# op 是 '+' '-' '*' '/' 其中之一
# a b 分别是 2 个数字
# 根据 op 对 a b 运算并返回结果(加减乘除)
# def apply(op, a, b)
def apply(op, a, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    else:
        return


# 作业 12
# 实现 apply_list 函数
# op 是 '+' '-' '*' '/' 其中之一
# oprands 是一个只包含数字的 list
# 根据 op 对 oprands 中的元素进行运算并返回结果
# def apply(op, oprands)
# 例如, 下面的调用返回 -4
# apply('-', [3, 4, 2, 1])
def apply_list(op, oprands):
    # s = oprands[0]
    # for i in oprands[1:]:
    #     s = apply(op, s, i)
    # return s
    if op == '+':
        s = 0
        for i in oprands:
            s += i
        return s
    elif op == '-':
        s = 0
        for i in oprands:
            s -= i
        return s
    elif op == '*':
        s = 1
        for i in oprands:
            s *= i
        return s
    elif op == '/':
        s = oprands[0]
        for i in oprands[1:]:
            s /= i
        return s


# 作业 13
# 实现 apply_compare 函数
# 参数如下
# expression 是一个 list, 包含了 3 个元素
# 第一个元素是 op, 值是 '>' '<' '==' 其中之一
# 剩下两个元素分别是 2 个数字
# 根据 op 对数字运算并返回结果(结果是 True 或者 False)
# def apply_compare(expression)
def apply_compare(expression):
    op = expression[0]
    a = expression[1]
    b = expression[2]
    # 可以缩写为下面的形式
    # 但是左边的变量数量一定要完全等于右边的长度
    # op, a, b = expression
    if op == '>':
        return a > b
    elif op == '<':
        return a < b
    elif op == '==':
        return a == b


# 注意
# 下面两题做不出来没关系
#
# 作业 14
# 实现 apply_if 函数
# 参数如下
# expression 是一个 list, 包含了 4 个元素
# 第一个元素是 'if' (也就是 op)
# 第二个元素是 'True' 或者 'False'
#
# 如果第二个元素的结果是 True 则返回第三个元素
# 否则返回第四个元素
# def apply_if(expression)
def apply_if(expression):
    op, condition, a, b = expression
    if op == 'if':
        if condition == 'True':
            return a
        else:
            return b


# 作业 15
# 实现 apply_all 函数
# 参数如下
# expression 是一个 list
# expression 中第一个元素是上面几题的 op, 剩下的元素是和 op 对应的值
# 根据 expression 运算并返回结果
# def apply_all(expression)
def apply_all(expression):
    op = expression[0]
    # print('debug', op)
    if op in '+-*/':
        # print('op in /')
        return apply_list(op, expression[1:])
    elif op in ['>', '<', '==']:
        return apply_compare(expression)
    elif op == 'if':
        return apply_if(expression)


# 作业 3.6
# 更新 apply_if, 描述见 docstring
# 本题没有提示, 做不出来就不要做
#
def apply_if(expression):
    '''
    expression 有 3 个元素
    第一个元素是布尔值 True False 或者是一个可以作为 apply_compare 参数的表达式
    如果 True 或者 apply_compare 的返回值是 True, 返回第 2 个元素
    否则, 返回第 3 个元素

    # 注意, 判断类型可以用 type 函数
    type(1) == type(100)
    type([1,2,3]) == type([])

    :return: 根据第一个元素的值返回不同的元素
    '''
    if expression[0]:
        return expression[1]
    else:
        return expression[2]


# 测试函数
def test_apply_if():
    ensure(apply_if([1 == 2, 2, 3]) == 3, '测试1')
    ensure(apply_if([2 == 2, 2, 3]) == 2, '测试2')


test_apply_if()

# =====
# 提示
# =====
'''
3.1
    先循环求出 list 中最长的元素的长度
    再用循环处理每个元素并添加进一个新的 list


3.2
top
    写一个辅助函数 compare 来比较两个字典的大小
    请参考上课的预习中字典的使用方法


3.3
formated_weekday
    用字典存储, 用 str 把参数转为字符串来当做 key 取对应的数据


3.4
discount
    将折扣数值存储在字典中, 方便取用
    因为有默认值的存在, 所以使用 get 函数来设置默认值


3.5
index_of_max
    循环比较, 只不过保存的是下标, 所以换一种思路

'''
