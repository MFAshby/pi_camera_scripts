import socket
import sys

CAMERA_PORT = 8005
CAMERA_HOST = 'localhost'

def capture_image():
    with socket.socket() as sock:
        sock.connect((CAMERA_HOST, CAMERA_PORT))
        return recvall(sock)

def recvall(sock):
    buf = b''
    data = True
    while data:
        data = sock.recv(1024)
        buf += data
    return buf

