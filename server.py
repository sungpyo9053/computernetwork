import socket
import sys
from threading import Thread

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 3000))
server_socket.listen(0)
client_socket, addr = server_socket.accept()


def client1():



    while(True):

        data = client_socket.recv(1024)
        received = str(data, encoding='utf-8')
        print('client : {0}'.format(received))
        data = input('server : ')
        data = data.encode('utf-8')
        client_socket.sendall(data)




    client_socket.close()






if __name__=='__main__':



    print('run server...')


    client1()


    server_socket.close()
    sys.exit()
