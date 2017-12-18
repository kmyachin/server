#-*- coding: utf-8 -*-
import socket

def _main():
    sock = socket.socket()
    # TODO занести в параметры запуска порт
    sock.bind(('localhost',10000))
    sock.listen(1)

    while True:
        conn, addr = sock.accept()
        try:
            print "connection from: ", addr
            data = conn.recv(1024)
            if data:
                conn.sendall(data)
            else:
                break
        finally:
            conn.close()

if __name__ == '__main__':
    try:
        _main()
    except KeyboardInterrupt:
        print "Exiting..."