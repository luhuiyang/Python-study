# coding: utf-8

import socket

"""
2017/02/16
作业 1


资料:
在 Python3 中，bytes 和 str 的互相转换方式是
str.encode('utf-8')
bytes.decode('utf-8')

send 函数的参数和 recv 函数的返回值都是 bytes 类型
其他请参考上课内容, 不懂在群里发问, 不要憋着
"""


# 1
# 补全函数
def protocol_of_url(url):
    '''
    url 是字符串, 可能的值如下
    'g.cn'
    'g.cn/'
    'g.cn:3000'
    'g.cn:3000/search'
    'http://g.cn'
    'https://g.cn'
    'http://g.cn/'

    返回代表协议的字符串, 'http' 或者 'https'
    '''
    if url.split(':')[0] == 'https':
        return 'https'
    return 'http'


# 2
# 补全函数
def host_of_url(url):
    '''
    url 是字符串, 可能的值如下
    'g.cn'
    'g.cn/'
    'g.cn:3000'
    'g.cn:3000/search'
    'http://g.cn'
    'https://g.cn'
    'http://g.cn/'

    返回代表主机的字符串, 比如 'g.cn'
    '''
    if url[:5] == 'https':
        url = url[8:]
    elif url[:4] == 'http':
        url = url[7:]
    end = url.find('/')
    if end != -1:
        url = url[:end]
    elif end == 1 & url.find(':') != -1:
        url = url[:url.find(':')]
    return url


# 3
# 补全函数
def port_of_url(url):
    '''
    url 是字符串, 可能的值如下
    'g.cn'
    'g.cn/'
    'g.cn:3000'
    'g.cn:3000/search'
    'http://g.cn'
    'https://g.cn'
    'http://g.cn/'

    返回代表端口的字符串, 比如 '80' 或者 '3000'
    注意, 如上课资料所述, 80 是默认端口
    '''
    port = 80
    if url[:5] == 'https':
        url = url[8:]
    elif url[:4] == 'http':
        url = url[7:]
    if url.find(':') != -1:
        url = url[url.find(':') + 1:]
        port = url.split('/')[0]
    return port


# 4
# 补全函数
def path_of_url(url):
    '''
    url 是字符串, 可能的值如下
    'g.cn'
    'g.cn/'
    'g.cn:3000'
    'g.cn:3000/search'
    'http://g.cn'
    'https://g.cn'
    'http://g.cn/'

    返回代表路径的字符串, 比如 '/' 或者 '/search'
    注意, 如上课资料所述, 当没有给出路径的时候, 默认路径是 '/'
    '''
    path = '/'
    host = host_of_url(url)
    url = url[url.find(host):]
    if url.find('/') != -1:
        path = url[url.find('/'):]
    return path


# 4
# 补全函数
def parsed_url(url):
    '''
    url 是字符串, 可能的值如下
    'g.cn'
    'g.cn/'
    'g.cn:3000'
    'g.cn:3000/search'
    'http://g.cn'
    'https://g.cn'
    'http://g.cn/'
    返回一个 tuple, 内容如下 (protocol, host, port, path)
    '''
    return (protocol_of_url(url), host_of_url(url), port_of_url(url), path_of_url(url))


# 5
# 把向服务器发送 HTTP 请求并且获得数据这个过程封装成函数
# 定义如下
def get(url):
    '''
    本函数使用上课代码 client.py 中的方式使用 socket 连接服务器
    获取服务器返回的数据并返回
    注意, 返回的数据类型为 bytes
    '''
    s = socket.socket()
    protocol, host, port, path = parsed_url(url)

    # 用 connect 函数连接上主机
    s.connect((host, port))

    # 构造一个 HTTP 请求
    http_request = 'GET / HTTP/1.1\r\nhost:{}\r\n\r\n'.format(host)

    # 发送 HTTP 请求给服务器
    # send 函数只接受 bytes 作为参数
    # str.encode 把 str 转换为 bytes, 编码是 utf-8
    request = http_request.encode('utf-8')
    s.send(request)

    response = s.recv(1000)
    return response


# 使用
def main():
    url = 'http://movie.douban.com/top250'
    r = get(url)
    print(r)


if __name__ == '__main__':
    main()
