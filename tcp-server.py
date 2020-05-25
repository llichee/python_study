import socket

def main():
    #创建tcp套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #绑定
    tcp_socket.bind(("", 7890))

    #将套接字设置为监听状态
    tcp_socket.listen(128)

    #等待客户端的链接
    client_socket, clientAddr = tcp_socket.accept()

    print(clientAddr)

    #接收客户端发送过来的请求
    recv_data = client_socket.recv(1024)
    print(recv_data)

    client_socket.send("INFO:ending...".encode("utf-8"))

    client_socket.close()
    tcp_socket.close()



if __name__ == "__main__":
    main()