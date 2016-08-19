from lxml import html
import requests
import socket
import ssl


def log(*args):
    if 0 == 0:
        print(*args)


class Model(object):
    def __repr__(self):
        class_name = self.__class__.__name__
        properties = ('{} = {}'.format(k, v) for k, v in self.__dict__.items())
        result = '\n<{}:\n {}\n'.format(class_name, '\n'.join(properties))
        return result


class Answer(Model):
    def __init__(self):
        self.author = ''
        self.content = ''
        self.link = ''
        self.img = []


def parsed_url(url):
    """
    解析 url 返回 (protocol host port path)
    有的时候有的函数, 它本身就美不起来, 你要做的就是老老实实写
    """
    # 检查协议
    protocol = 'http'
    if url[:7] == 'http://':
        u = url.split('://')[1]
    elif url[:8] == 'https://':
        protocol = 'https'
        u = url.split('://')[1]
    else:
        # '://' 定位 然后取第一个 / 的位置来切片
        u = url

    # 检查默认 path
    i = u.find('/')
    if i == -1:
        host = u
        path = '/'
    else:
        host = u[:i]
        path = u[i:]

    # 检查端口
    port_dict = {
        'http': 80,
        'https': 443,
    }
    # 默认端口
    port = port_dict[protocol]
    if host.find(':') != -1:
        h = host.split(':')
        host = h[0]
        port = int(h[1])

    return protocol, host, port, path


def socket_by_protocol(protocol):
    """
    根据协议返回一个 socket 实例
    """
    if protocol == 'http':
        s = socket.socket()
    else:
        # HTTPS 协议需要使用 ssl.wrap_socket 包装一下原始的 socket
        # 除此之外无其他差别
        s = ssl.wrap_socket(socket.socket())
    return s


def response_by_socket(s):
    """
    参数是一个 socket 实例
    返回这个 socket 读取的所有数据
    """
    response = b''
    buffer_size = 1024
    while True:
        r = s.recv(buffer_size)
        if len(r) == 0:
            break
        response += r
    return response


def parsed_response(r):
    """
    把 response 解析出 状态码 headers body 返回
    状态码是 int
    headers 是 dict
    body 是 str
    """
    header, body = r.split('\r\n\r\n', 1)
    h = header.split('\r\n')
    status_code = h[0].split()[1]
    status_code = int(status_code)

    headers = {}
    for line in h[1:]:
        k, v = line.split(': ')
        headers[k] = v
    return status_code, headers, body


# 复杂的逻辑全部封装成函数
def get(url):
    """
    用 GET 请求 url 并返回响应
    """
    protocol, host, port, path = parsed_url(url)
    s = socket_by_protocol(protocol)
    s.connect((host, port))

    cookie = '_zap=bbb05cca-c401-455e-abbc-15ae5f661b41; ___rl__test__cookies=1467594847261; d_c0="AEBAwykNJAqPTsQlE3ZCsaBOGFYDBt53B6s=|1466998061"; _za=28d62bca-d359-4dca-8513-9cf818b50b41; _zap=fb2c7083-2d0e-40ba-a860-12f578b15bf2; OUTFOX_SEARCH_USER_ID_NCOO=1745703702.4768739; q_c1=55af333393c34fe6bd164c02a2506928|1470017348000|1466998061000; _xsrf=256fbbc9ad8fea781ab6e277d4672009; l_cap_id="YzY3NGUwZjJkYzA3NGEzMmExYTkzYjY2ZjkwYTBiMjc=|1470022210|9431b38ab509dbc70283ab02729f67ef4755d7e8"; cap_id="NGI3NDY4NTBmOGY5NDYyMWI5YzA5N2UxMTNiZTRjMmY=|1470022210|ee158baeef9a686ed90fe8a9afe6b5349584f67c"; login="NTQzZTczYWE0ZmM1NGYzY2JmMDA2ZDVjMDFhYTRlZWI=|1470022214|ae7dcda50e24d72e26f0503bab91c042784d9edc"; n_c=1; s-q=%E4%B8%BA%E4%BB%80%E4%B9%88%E5%BE%88%E5%A4%9A%E4%BA%BA%E6%89%B9%E8%AF%84%E5%B0%8F%E7%B1%B3%E6%89%8B%E6%9C%BA; s-i=1; sid=1rjcakko; __utmt=1; __utma=51854390.458161178.1471596504.1471596504.1471596504.1; __utmb=51854390.14.10.1471596504; __utmc=51854390; __utmz=51854390.1471596504.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.100-1|2=registration_date=20130605=1^3=entry_date=20130605=1; a_t="2.0AADAmcUbAAAXAAAAq1neVwAAwJnFGwAAAEBAwykNJAoXAAAAYQJVTUZPxlcAK_L4c7LXtO1yLPJSuB66wJ1f4HgeyuX-VShySGozHogPqlCNhbZ1UA=="; z_c0=Mi4wQUFEQW1jVWJBQUFBUUVEREtRMGtDaGNBQUFCaEFsVk5Sa19HVndBcjh2aHpzdGUwN1hJczhsSzRIcnJBblZfZ2VB|1471597739|a754a51ded7841d96157a245d8d270eca272bf78'
    userAgent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'

    request = 'GET {} HTTP/1.1\r\nhost: {}\r\nUser-Agent: {}\r\nCookie: {}\r\nConnection: close\r\n\r\n'.format(path,
                                                                                                                host,
                                                                                                                userAgent,
                                                                                                                cookie)
    encoding = 'utf-8'
    s.send(request.encode(encoding))

    response = response_by_socket(s)
    log('response', response)
    r = response.decode(encoding)

    status_code, headers, body = parsed_response(r)
    if status_code == 301:
        url = headers['Location']
        return get(url)
    return status_code, headers, body


def answer_from_div(div):
    a = Answer()
    a.author = div.xpath('.//a[@class="author-link"]')[0].text
    log('author, ', a)
    content = div.xpath('.//div[@class="zm-editable-content clearfix"]/text()')
    a.content = '\n'.join(content)
    # log('ssssrc', div.xpath('.//div[@class="zm-editable-content clearfix"]/img/@src'))
    a.img = div.xpath('.//div[@class="zm-editable-content clearfix"]/img/@data-original')
    # log('src', a.img[0])
    download_image(a.img)
    return a


def divs_from_url(url):
    _, _, body = get(url)
    root = html.fromstring(body)
    divs = root.xpath('//div[@class="zm-item-answer  zm-item-expanded"]')
    log('divs', len(divs))
    log('divs', divs[0])
    items = [answer_from_div(div) for div in divs]


def download_image(imgs):
    for m in imgs:
        r = requests.get(m)
        path = 'xxx/' + m.split('/')[-1]
        with open(path, 'wb') as f:
            f.write(r.content)


def main():
    # url = 'https://www.zhihu.com/question/37709992'
    url = 'https://www.zhihu.com/question/30594270'
    divs_from_url(url)


if __name__ == '__main__':
    main()
