import socket
import time
from multiprocessing import Process


class EchoServer:
    def __init__(self, host, port, timeout=5000):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.conn = None
    #

    def __enter__(self):
        self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return self
    #

    def run(self):
        self.tcp_socket.bind((self.host, self.port))
        self.tcp_socket.listen()
        self.conn, addr = self.tcp_socket.accept()
        # start_time = time.time()
        with self.conn:
            print('[EchoServer] Connected by {}'.format(addr))
            while True:
                data = self.conn.recv(1024)
                if not data:
                    break
                #
                self.conn.sendall(data)
                # elapsed_time = time.time() - start_time
                # if elapsed_time > self.timeout:
                #     break
                # #
            #
        #
    #

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('[EchoServer] Existing...')
        self.conn.close()
        self.tcp_socket.close()
    #
#


class EchoClient:
    def __init__(self, server_host, server_port):
        self.server_host = server_host
        self.server_port = server_port
        pass
    #

    def __enter__(self):
        self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return self
    #

    def send(self):
        self.tcp_socket.connect((self.server_host, self.server_port))
        for i in range(5):
            time.sleep(1)
            msg = 'Message {}'.format(i)
            self.tcp_socket.sendall(msg.encode())
            data = self.tcp_socket.recv(1024)
            print('[EchoClient] Received {}'.format(repr(data)))
        #
        self.tcp_socket.sendall(b'')
    #

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.tcp_socket.close()
    #
#


def run_client():
    with EchoClient('127.0.0.1', 10083) as ec:
        ec.send()
    #
#


if __name__ == '__main__':
    p = Process(target=run_client)
    p.start()

    with EchoServer('127.0.0.1', 10083) as s:
        s.run()
    #
#
