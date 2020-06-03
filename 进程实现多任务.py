import multiprocessing
import time

"""多进程实现多任务"""

def test1():
    while True:
        print("test1......")
        time.sleep(1)

def test2():
    while True:
        print("test2......")
        time.sleep(1)

def main():
    """实例化两个对象，target指定函数名，注意函数名不要带括号"""
    t1 = multiprocessing.Process(target=test1)
    t2 = multiprocessing.Process(target=test2)

    """创建两个进程"""
    t1.start()
    t2.start()

if __name__ == "__main__":
    main()
