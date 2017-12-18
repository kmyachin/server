#-*- coding: utf-8 -*-
import socket

def client():
    server_addr = ('localhost', 10000)
    sock = socket.create_connection(server_addr)

    try:
        message = "This is duplicate message"
        print message
        sock.sendall(message)
        received = 0
        expected = len(message)
        while received < expected:
            data = sock.recv(16)
            received += len(data)
            print "received ", data

    finally:
        print "closing socket..."
        sock.close()

if __name__ == '__main__':
    try:
        client()
    except KeyboardInterrupt:
        print "Exiting..."