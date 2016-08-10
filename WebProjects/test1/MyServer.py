import socket

s = socket.socket()

host = ''
port = 2001

s.bind((host, port))

request = b''
while True:
    s.listen(5)
    connection, address = s.accept()
    r = connection.recv(1024)
    if len(r) == 0:
        continue
    request += r

    request = request.decode('utf-8')
    results = request.split('\n')
    first_line = results[0]
    path = results[1]

    print('line', first_line)
    print('path', path)

    response = 'hahahahahaha'.encode('utf-8')
    connection.send(response)
    connection.close()