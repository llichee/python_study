import socket

def main():
    #创建tcp套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #链接服务器
    tcp_socket.connect(("192.168.7.27", 8080))

    #发送数据
    send_data = input("请输入要发送的内容：")
    tcp_socket.send(send_data.encode("utf-8"))

    #关闭套接字
    tcp_socket.close()

if __name__ == "__main__":
    main()