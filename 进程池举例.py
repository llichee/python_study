from multiprocessing import Pool
import os, time, random

def worker(msg):
    #记录开始时间
    t_start = time.time()
    #打印进程号
    print("%s 开始执行，进程号是 %d" % (msg, os.getpid()))
    #random.random()表示0-1的浮点数
    time.sleep(random.random()*2)
    #记录结束时间
    t_stop = time.time()
    #结束时间与开始时间的差，即为耗时
    print(msg, "执行完毕， 耗时%0.2f" % (t_stop - t_start))

#创建进程池，池内允许有3个进程
po = Pool(3)

for i in range(0,10):
    #将worker放入进程池中，并且将i作为参数传入
    po.apply_async(worker, (i,))

print("---start---")
#关闭进程池
po.close()
#关闭主进程
po.join()
print("---stop---")