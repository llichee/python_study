import socket
import re

def server_client(new_socket):

    #接收浏览器发来的数据，记得解码
    request = new_socket.recv(1024).decode("utf-8")
    #将从浏览器发来的数据转化为列表，并且是每行一个元素的形式
    request_list = request.splitlines()
    print(">>>" * 10)
    print(request_list)

    #正则匹配浏览器发来的数据的第一个元素，然后提取相应的网站根路径
    #GET /index.html HTTP/1.1

    ret = re.match(r"[^/]+([^ ]*)", request_list[0])

    #如果匹配到对应的正则，即将网站根路径赋给file_name，如果匹配到/，即将index.html赋给file_name
    file_name = ""
    if ret:
        file_name = ret.group(1)
        if file_name == "/":
            file_name = "/index.html"


    #此处注意try  except  else的用法；
    #主要定义的是服务器端返给浏览器的内容
    try:
        #以二进制的格式读取html下的ret，该ret变量是访问网站的时候ip地址后跟的路径，例如127.0.0.1:7788/index.html
        f = open("./html" + ret, "rb")
    except:
        #如果上一步没有返回值，则执行如下代码，返回给浏览器404
        response = "HTTP/1.1 404 Not Found\r\n"
        response += "\r\n"
        response += "---File Not Found---"
        new_socket.send(response.encode("utf-8"))
    else:
        #如果try下的代码执行成功，有返回值，则执行如下代码，返给浏览器相应的内容
        response = "HTTP/1.1 200 OK\r\n"
        response += "\r\n"
        response_connect = f.read()
        f.close()
        new_socket.send(response.encode("utf-8"))
        new_socket.send(response_connect)

    new_socket.close()

def main():
    #创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    #绑定地址和端口
    tcp_socket.bind(("", 7789))

    #转为监听状态
    tcp_socket.listen(128)

    while True:
        #等待客户端连接
        new_socket, client_addr = tcp_socket.accept()

        # 客户端请求
        server_client(new_socket)

    tcp_socket.close()

if __name__ == "__main__":
    main()