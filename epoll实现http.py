import socket
import re
import select

def service_client(new_socket, request):

    request_lines = request.splitlines()
    print("")
    print(">" * 20)
    print(request_lines)

    # GET /index.html HTTP/1.1
    # get post put del
    file_name = ""
    ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
    if ret:
        file_name = ret.group(1)
        print("*" * 50, file_name)
        if file_name == "/":
            file_name = "/index.html"

    # 返回http格式的数据， 给浏览器

    try:
        f = open("./html" + file_name, "rb")
    except:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += "\r\n"
        response += "---File Not Found---"
        new_socket.send(response.encode("utf-8"))
    else:
        html_content = f.read()
        f.close()

        response_body = html_content

        response_header = "HTTP/1.1 200 OK\r\n"
        response_header += "Content-Length:%d\r\n" % len(response_body)
        response_header += "\r\n"

        response = response_header.encode("utf-8") + response_body

        new_socket.send(response)

def main():
    #创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #绑定端口
    tcp_server_socket.bind(("", 7788))

    #变为监听套接字
    tcp_server_socket.listen(128)

    #将套接字变为非阻塞
    tcp_server_socket.setblocking(False)

    #创建一个epoll对象
    epl = select.epoll()

    #将监听套接字对应的fd(文件描述符)注册到epoll中
    epl.register(tcp_server_socket.fileno(), select.EPOLLIN)

    #创建一个空字典
    fd_event_dict = dict()

    while True:
        fd_event_list = epl.poll()  # 默认会阻塞，知道os监测到数据到来  通过时间通知方式 告诉这个程序，此时才会解阻塞

        # [(fd, event), (套接字对应的文件描述符， 这个文件描述符到底是什么事件，例如 可以调用recv接收等)]
        for fd, event in fd_event_list:
            #等待新的客户端的链接
            new_socket, client_addr = tcp_server_socket.accept()
            epl.register(new_socket.fileno(), select.EPOLLIN)
            fd_event_dict[new_socket.fileno()] = new_socket
        elif event == select.EPOLLIN:
            #判断已经链接的客户端是否有数据发送过来
            recv_data = fd_event_dict[fd].recv(1024).decode("utf-8")
            if recv_data:
                service_client(fd_event_dict[fd], recv_data)
            else:
                fd_event_dict[fd].close()
                epl.unregister(fd)
                def fd_event_dict[fd]

    tcp_server_socket.close()

if __name__ == "__main__":
    main()