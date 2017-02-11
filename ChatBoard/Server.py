from tornado.tcpserver import TCPServer
from tornado.ioloop import IOLoop


class NewUser(object):
    def __init__(self, address, stream):
        self._stream = stream
        self._address = address
        self._stream.set_close_callback(self.bye)
        self.read()

    def read(self):
        self._stream.read_until(b'\n', self.display)

    def display(self, msg):
        print('%s: %s' % (self._address, msg.decode().strip()))
        self.read()

    def bye(self):
        print('%s left us...' % (self._address,))


class ChatServer(TCPServer):
    def handle_stream(self, stream, address):
        print('New connection from %s' % (address,))
        NewUser(address, stream)


server = ChatServer()
server.listen(8000)
IOLoop.instance().start()
