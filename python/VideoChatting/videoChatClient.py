import socket
import numpy as np
import cv2
from _thread import *
from queue import Queue

enclosure_queue = Queue()

def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf

HOST = '165.229.185.201'
PORT = 9999
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

def webcam(queue):
    capture = cv2.VideoCapture(0)
    while True:
        ret, frame = capture.read()
        if ret == False:
            continue

        encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]
        result, imgencode = cv2.imencode('.jpg', frame, encode_param)
        data = np.array(imgencode)
        stringData = data.tobytes()
        queue.put(stringData)
        cv2.imshow('image', frame)

        key = cv2.waitKey(1)
        if key == 27: # if ESC key is input, then exit
            break

def sendIMG(client_socket, queue):
    while True:
        try:
            stringData = queue.get()
            client_socket.send(str(len(stringData)).ljust(16).encode())
            client_socket.send(stringData)
        except ConnectionResetError as e:
            break
    client_socket.close()

def recvIMG(client_socket):
    while True:
        length = recvall(client_socket,16)
        stringData = recvall(client_socket, int(length))
        data = np.frombuffer(stringData, dtype='uint8')
        decimg=cv2.imdecode(data,1)
        cv2.imshow('Image',decimg)

        key = cv2.waitKey(1)
        if key == 27: # if ESC key is input, then exit
            break
    client_socket.close()

start_new_thread(webcam, (enclosure_queue,))
start_new_thread(sendIMG, (client_socket, enclosure_queue,))
start_new_thread(recvIMG, (client_socket, ))
