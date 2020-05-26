import socket

def main():
    #创建tcp套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #绑定
    tcp_socket.bind(("", 7890))

    #将套接字设置为监听状态
    tcp_socket.listen(128)

    #循环目的：调用多次accept，从而为多个客户端服务
    while True:
        #等待客户端的链接
        print("INFO：wait clienting...")
        #等待客户端的连接，accept阻塞在这里，客户端连接成功后继续往下进行
        client_socket, clientAddr = tcp_socket.accept()

        print(clientAddr)

        #循环目的：为同一个客户端服务多次
        while True:
            #接收客户端发送过来的请求
            recv_data = client_socket.recv(1024)
            print("Client data: %s " % str(recv_data.decode("utf-8")))

            #如果收到客户端发来的数据，则回送给客户端一个数据
            #否则就break
            if recv_data:
                client_socket.send("INFO:ending...".encode("utf-8"))
            else:
                break
        client_socket.close()
    tcp_socket.close()



if __name__ == "__main__":
    main()