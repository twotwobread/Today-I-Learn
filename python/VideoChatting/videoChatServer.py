import socket
import cv2
import numpy
from queue import Queue
from _thread import *
import time

enclosure_queue = Queue()

def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf

def sendIMG(client_socket, addr, queue):
    print('Connected by :', addr[0], ':', addr[1])
    while True:
        try:
            #data = client_socket.recv(1024)
            #if not data:
              #  print('Disconnected by ' + addr[0],':',addr[1])
               # break
            stringData = queue.get()
            client_socket.send(str(len(stringData)).ljust(16).encode())
            client_socket.send(stringData)
        except ConnectionResetError as e:
            print('Disconnected by ' + addr[0],':',addr[1])
            break
    client_socket.close()
    
def webcam(queue):
    capture = cv2.VideoCapture(0)
    while True:
        ret, frame = capture.read()
        if ret == False:
            continue

        encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]
        result, imgencode = cv2.imencode('.jpg', frame, encode_param)
        data = numpy.array(imgencode)
        stringData = data.tobytes()
        queue.put(stringData)
        cv2.imshow('image', frame)

        key = cv2.waitKey(1)
        if key == 27: # if ESC key is input, then exit
            break

def recvIMG(client_socket):
    while True:
        length = recvall(client_socket,16)
        stringData = recvall(client_socket, int(length))
        data = numpy.frombuffer(stringData, dtype='uint8')
        decimg=cv2.imdecode(data,1)
        cv2.imshow('Image',decimg)

        key = cv2.waitKey(1)
        if key == 27: # if ESC key is input, then exit
            break
    client_socket.close()
    
HOST = '165.229.185.201'
PORT = 9999
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen()

print('server start')
start_new_thread(webcam, (enclosure_queue,))
client_socket, addr = server_socket.accept()
start_new_thread(sendIMG, (client_socket, addr, enclosure_queue,))
start_new_thread(recvIMG, (client_socket, ))
#server_socket.close()
