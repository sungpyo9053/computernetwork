import socket

if __name__=="__main__":
    data_transferred=0

    sock = socket.socket(socket.AF_INET,
                         socket.SOCK_STREAM)  # SOCK_STREAM은 TCP socket을 뜻함

    sock.connect(('127.0.0.1', 3000))

    filename = input('업데이트할 파일이름을 입력하세요:')
    sock.sendall(filename.encode())

    with open('download/' + filename, 'rb') as f:
        try:
            data = f.read()  # 파일을 1024바이트 읽음
            sock.sendall(data)
            data_transferred=len(data)
        except Exception as e:
            print(e)
    print('파일[%s] 전송종료. 전송량 [%d]' % (filename, data_transferred))
