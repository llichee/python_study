import socket

def send_file_2_client(new_client_socket, client_addr):
    # 1.接收客户端发送过来的要下载的文件名
    file_name = new_client_socket.recv(1024).decode("utf-8")
    print("客户端(%s)需要下载的文件是: %s" % (str(client_addr), file_name))

    file_content = None
    #2.打开这个文件，读取数据
    try:
        f = open(file_name, "rb")
        file_content = f.read()
        f.close()
    except Exception as ret:
        print("没有要下载的文件（%s）" % file_name)

    #3. 发送文件的数据给客户端
    if file_content:
        new_client_socket.send(file_content)


def main():
    #创建tcp套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #绑定
    tcp_socket.bind(("", 7890))

    #将套接字设置为监听状态
    tcp_socket.listen(128)

    while True:
        #等待客户端的链接 accept
        new_client_socket, client_addr = tcp_socket.accept()

        #调用发送文件函数，完成为客户端服务
        send_file_2_client(new_client_socket, client_addr)

        #关闭套接字
        new_client_socket.close()
    tcp_socket.close()



if __name__ == "__main__":
    main()