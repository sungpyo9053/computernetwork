import socket
bindIP = input('IP:')
def runServer():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((bindIP,3000))
    server_socket.listen(0)
    client_socket, addr = server_socket.accept()
    print('++++++파일 서버를 시작++++++')
    print("+++파일 서버를 끝내려면 'Ctrl + C'를 누르세요.")
    filename = client_socket.recv(1024)
    data = client_socket.recv(1024)
    if not data:
        print('파일[%s]: 서버에 존재하지 않거나 전송중 오류발생' % filename)
        return

    with open(filename, 'wb') as f:
        try:
            while data:
                f.write(data)

                data = client_socket.recv(1024)
        except Exception as e:
            print(e)



runServer()
