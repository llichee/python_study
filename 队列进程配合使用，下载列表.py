import multiprocessing

def download_data(q):
    """下载数据"""
    data = [45, 56, 2, 3]

    #向队列中写入数据
    for temp in data:
        q.put(temp)
    print("数据下载完成！")

def recv_data(q):
    """数据处理"""
    recv_list = list()  #创建空列表，用来存数据
    #从队列中获取数据
    while True:
        dataa = q.get()
        recv_list.append(dataa)
        #判断队列中是否还有数据，如果没有则终止循环
        if q.empty():
            break

    print(recv_list)


def main():

    #创建一个队列
    q = multiprocessing.Queue()

    #实例化对象
    t1 = multiprocessing.Process(target=download_data,args=(q,))
    t2 = multiprocessing.Process(target=recv_data,args=(q,))
    #创建两个进程
    t1.start()
    t2.start()

if __name__ == "__main__":
    main()
