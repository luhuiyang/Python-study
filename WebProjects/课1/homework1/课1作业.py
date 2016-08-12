import socket

"""
作业 1
8.10

请参考上课板书内容
"""


def log(*args):
    print(*args)


# 1
# 补全函数 parsed_url
def parsed_url(url):
    '''
    url 可能的值如下
    g.cn
    g.cn/
    g.cn:3000
    g.cn:3000/search
    http://g.cn
    https://g.cn
    http://g.cn/

	NOTE:
    没有 protocol 时, 默认协议是 http

    在 http 下 默认端口是 80
    在 https 下 默认端口是 443
    :return : tuple, 内容如下 (protocol, host, port, path)
    '''
    protocol_map = {
        'http': 'http',
        'https': 'https',
    }
    protocol = ''
    port = 0
    host = ''
    path = ''
    temp = ''
    numbers = '0123456789'
    protocol = 'http'
    start_position = 0
    if url.split(':')[0] == 'http':
        start_position = 7
    elif url.split(':')[0] == 'https':
        protocol = 'https'
        start_position = 8

    host, port, path = get_port(protocol, url[start_position:])
    return (protocol, host, port, path)


def get_port(protocol, url):
    """

    :param protocol:协议
    :param url: 不含协议：//的url
    :return: 主机， 端口， 路径
    """
    path = ''
    port = 0
    host = ''
    # log('url2 == ', url)
    position = url.find('/')
    if position != -1:
        path = url[position:]
    else:
        # log('无路径')
        position = len(url)
    host, port = get_host_port(protocol, url[:position])
    return host, port, path


def get_host_port(protocol, url):
    """

    :param protocol
    :param url: 不含协议和路径的url
    :return: host port
    """

    # log('url3 == ', url)
    port = 0
    host = ''
    position = url.find(":")
    # log('protocol = ', protocol)
    if position == -1:
        host = url
        if protocol == 'http':
            port = 80
        else:
            port = 443
    else:
        host = url[:position]
        port = int(url[(position + 1):])
    return host, port


log('result')
log('结果', parsed_url('g.cn'))
log('结果', parsed_url('g.cn/'))
log('结果', parsed_url('g.cn:3000'))
log('结果', parsed_url('g.cn:3000/search'))
log('结果', parsed_url('http://g.cn'))
log('结果', parsed_url('https://g.cn'))
log('结果', parsed_url('http://g.cn/'))


# 2
# 把向服务器发送 HTTP 请求并且获得数据这个过程封装成函数
# 定义如下
def get(url):
    '''
    返回的数据类型为 bytes
    '''
    protocol, host, port, path = parsed_url(url)
    log('数据', parsed_url(url))
    s = socket.socket()

    s.connect((host, port))

    myIp, myPort = s.getsockname()
    print('本机 ip 和 port {} {}'.format(myIp, myPort))

    request = 'GET {} HTTP/1.1\r\nhost:{}\r\nConnection:close\r\n\r\n'.format(path, host)

    log('request', request)
    request = request.encode('utf-8')
    s.send(request)
    response = b''
    while True:
        r = s.recv(1000)
        if len(r) == 0:
            break
        response += r

    result = response.decode('utf-8')
    return result


"""
资料:
在 Python3 中，bytes 和 str 的互相转换方式是
str.encode('utf-8')
bytes.decode('utf-8')

send 函数的参数和 recv 函数的返回值都是 bytes 类型
"""


# 使用
def main():
    url = 'http://movie.douban.com/top250'
    r = get(url)
    print(r)


if __name__ == '__main__':
    main()
