import gevent
import time
from gevent import monkey

"""协程最核心点，在于充分利用程序执行时，等待的时间，不阻塞"""

monkey.patch_all()   #开头打好补丁，然后下方就无需再挨个gevent.sleep(0.5)

def f1(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        #gevent.sleep(0.5)
        time.sleep(0.5)

def f2(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        #gevent.sleep(0.5)
        time.sleep(0.5)

def f3(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        #gevent.sleep(0.5)
        time.sleep(0.5)

print("---1---")
g1 = gevent.spawn(f1, 5)
print("---2---")
g2 = gevent.spawn(f2, 5)
print("---3---")
g3 = gevent.spawn(f3, 5)
print("---4---")

#g1.join()
#g2.join()
#g3.join()

g = [g1, g2, g3]

gevent.joinall(g)    #将多个任务存入一个列表中，就无需挨个写g1.join()了