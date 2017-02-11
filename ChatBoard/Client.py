import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 8000))

while True:
    try:
        inp = (input('localhost: ') + '\n').encode()
        s.send(inp)
    except KeyboardInterrupt:
        print('break from user')
        break
s.shutdown(socket.SHUT_RDWR)
s.close()