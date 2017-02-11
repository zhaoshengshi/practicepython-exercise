import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 8000))

while True:
    try:
        inp = input('localhost: ') + '\n'
        s.send(inp.encode())
    except (KeyboardInterrupt, ConnectionResetError):
        print('Disconnected...')
        break


s.shutdown(socket.SHUT_RDWR)
s.close()