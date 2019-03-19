import socket
from threading import Thread
import sys
from multiprocessing import Process
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1',0))
sock.connect(('127.0.0.1', 3000))
def send():



        
    str = input('client : ')
    str = str.encode('utf-8')
    sock.sendall(str)


def recive():



    data = sock.recv(1024)
    received = str(data, encoding='utf-8')

    print('server : {0}'.format(received))


if __name__=='__main__':



    while(True):
        send()
        recive()

    sock.close()
    sys.exit()





