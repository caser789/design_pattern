import socket
import gzip
from io import BytesIO


def response(client):
    response = raw_input("Enter a value: ")
    client.send(response)
    client.close()


class LogSock(object):

    def __init__(self, socket):
        self.socket = socket

    def send(self, data):
        print "sending {0} to {1}".format(data, self.socket.getpeername()[0])
        self.socket.send(data)

    def close(self):
        self.socket.close()


class GzipSock(object):

    def __init__(self, socket):
        self.socket = socket

    def send(self, data):
        buf = BytesIO()
        zipfile = gzip.GzipFile(fileobj=buf, mode='w')
        zipfile.write(data)
        zipfile.close()
        self.socket.send(buf.getvalue())

    def close(self):
        self.socket.close()

if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 2401))
    server.listen(1)
    try:
        while True:
            client, addr = server.accept()
            if log_send:
                client = LogSock(client)
            if client.getpeername()[0] in compress_hosts:
                client = GzipSock(client)
            response(client)
    finally:
        server.close()
