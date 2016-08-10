import socket

s = socket.socket()

host = 'www.9ji.com'
port = 80

s.connect((host, port))

ip, myport = s.getsockname()

print('本机ip: {} , 端口： {}'.format(ip, myport))

http_request = 'GET /help/8743.html HTTP/1.1\r\nhost: {}\r\nConnection: close\r\n\r\n'.format(host)

print('request', http_request)
request = http_request.encode('utf-8')

s.send(request)

response = b''
while True:
    r = s.recv(1024)
    if len(r) == 0:
        break
    response += r

response = response.decode('utf-8')

print('response', response)
