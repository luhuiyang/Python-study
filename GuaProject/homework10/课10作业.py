# 2016/7/28
#
# ========
# 作业 (实时更新)
#
# 注意, 作业会在这里实时更新, 有问题请评论
# 注意, 登录论坛后才有评论功能
# ========
# 7/28 更新 10.1
#
#
# 请直接在我的代码中更改/添加, 不要新建别的文件


# 重新定义我们的 log 函数
def log(*args):
    print(*args)


# ====
# 测试
# 如果没有测试, 自行编写
# ====


class Node(object):
    def __init__(self, element=0):
        self.element = element
        self.next = None


# 作业 10.1
# 5 分钟做不出就看提示
#
def length(node):
    '''
    node 是 Node 实例
    指向了其他的 Node 实例
	返回这一串 node 的数量

	:return: int
    '''
    count = 0
    while node != None:
        count += 1
        node = node.next
    return count



# 作业 10.2
#
def element_at_index(node, n):
    '''
    node 是 Node 实例

	返回第 n 个 Node 中存储的元素(下标从 0 开始)

    :return: Node 中存储的元素
    '''
    for i in range(n):
        node = node.next
    return node.element


# 作业 10.3
#
def append(node, element):
    '''
    node 是 Node 实例
	在末尾插入一个 element

    :return: None
    '''
    while node != None:
        node = node.next
    node = Node(element)
    return None


# 作业 10.4
#
def insert_after_index(node, index, element):
    '''
    node 是 Node 实例
    index 是 int
	在第 index 个元素后插入一个 element

    :return: None
    '''
    for i in range(index):
        node = node.next
    temp = Node(element)
    temp.next = node.next
    node.next = temp
    return


# 作业 10.5
#
def remove(head, element):
    '''
    head 是 Node 实例
	注意, head.next 才是第一个元素

	删除第一个出现的 element 节点

    :return: None
    '''
    node = head.next
    pre = head
    while node != None:
        if node.element == element:
            pre.next = node.next
            break
        else :
            pre = node
            node = pre.next
    return



# 作业 10.6
#
def remove_index(head, index):
    '''
    head 是 Node 实例
	注意, head.next 才是第一个元素

	删除第 index 个 Node
   	head.next 是第 0 个 Node

    :return: None
    '''
    pre = head
    node = head.next
    for i in range(index - 1):
        pre = node
        node = node.next
    pre.next = node.next
    return Node



# 作业 10.7
#
def remove_all(head, element):
    '''
    head 是 Node 实例
	注意, head.next 才是第一个元素

	删除所有出现的 element 节点

    :return: None
    '''
    node = head.next
    pre = head
    while node != None:
        if node.element == element:
            pre.next = node.next
            node = node.next
        else:
            pre = node
            node = pre.next
    return



# 作业 10.8
#
def reverse(head):
    '''
    head 是 Node 实例
	注意, head.next 才是第一个元素

	把这一串 Node 逆序

    :return: None
    '''
    temp = Node()
    node = head.next
    while node != Node:
        node.next = temp.next
        temp.next = node
        head.next = node.next
        node = node.next
    return


# 作业 10.9
#
def reverse1(node):
    '''
    node 是 Node 实例
	注意, node 是第一个元素, 并且 node 可能是 None

	把这一串 Node 逆序并返回

    :return:
    '''

    head = Node()
    head.next = node
    reverse(head)
    return head.next

# 作业 10.10
# 10 分钟可看提示
#
def delete_next(node):
    temp = node.next
    node.next = temp.next

def ytsefu(node, m=3):
    '''
    用链表实现约瑟夫环
    node 是 Node 实例, 里面存了从 0 开始递增的编号
	注意, node 是第一个元素
    最后一个元素的 next 是第一个元素
    也就是说, 它是一个环


	从第一个元素开始数, 数到 m 就发红包并移除

    返回最后一个得到红包的人的编号

    :return:
    '''
    while node.next != None:
        delete_next(node.next.next)
        node = node.next.next




# =====
# 提示
# =====
'''
10.1
length
    遍历计数


10.10
ytsefu
	定义一个辅助函数 delete_next
    计数 删除

'''
