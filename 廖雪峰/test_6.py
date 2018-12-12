class A:
    pass
"""***************************************************************进程/线程***************************************************************"""
# fork()只有在类Unix系统中有
import os,time,random
from multiprocessing import Process,Queue

def run_proc(name,y):
    """子进程要执行的代码"""
    print("Run child process %s%s(%s)"%(name,y,os.getpid()))

from multiprocessing import Pool

def long_time_task(name):
    print("Run task %s (%s)..." %(name,os.getpid()))
    start = time.time()
    time.sleep(random.random() * 30)
    end = time.time()
    print("Task %s runs %0.2f seconds."%(name,(end-start)))

import subprocess,os
# os.chdir(r'C:\Users\Administrator\Desktop\apache-jmeter-4.0\bin')
def ABCD():
    print("$ nslookup www.python.org")
    r = subprocess.call(['nslookup','www.python.org'])
    print("Exit code:%s" %r)
    r1 = subprocess.call(['jmeter.bat'])
    # print(r1)
    # print(str(r1).encode("gb2312"))

"""进程之间的通信Queue"""
def write(q):
    print("Process to write: %s"%os.getpid())
    for value in ["A","B","C"]:
        print("Put %s to queue..."%value)
        q.put(value)
        # time.sleep(random.random() * 5)
        time.sleep(1)

def read(q):
    print("Process to read: %s"%os.getpid())
    while True:
        value = q.get(True)
        print("Get %s from queue."%value)

"""***************************************************************线程***************************************************************"""
import threading
import multiprocessing
def loop():
    print("threading %s is running..."%threading.current_thread().name)
    n = 0
    while n < 5:
        n +=1
        print("thread %s >>> %s"%(threading.current_thread().name,n))
        time.sleep(1)
    print("thread %s ended."%threading.current_thread().name)

balance = 0
lock = threading.Lock()
def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(1000000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()

def for_for():
    i = 0
    while True:
        print(i)
        i += 1

if __name__ == '__main__':
    # print("Parent process %s" %os.getpid())
    # # args参数对相应的是target指向的函数要穿的参数（必须是元组方式）
    # p = Process(target=run_proc,args=('test','ysl'))
    #
    # print("All process will start")
    # p.start()
    # p.join()

    # print("Parent process %s."%os.getpid())
    # p = Pool(4)
    # for i in range(5):
    #     p.apply_async(long_time_task,args=(i,))
    # print("Waiting for all subprocess done...")
    # p.close()
    # p.join()
    # print("All subprocess done.")

    # ABCD()

    # q = Queue()
    # pw = Process(target=write,args=(q,))
    # pr = Process(target=read,args=(q,))
    # # pw.start()
    #
    # pr.start()
    # # pw.join()
    # pr.terminate()

    #######################线程###############
    # print("threading %s is running..."%threading.current_thread().name)
    # t = threading.Thread(target=loop,name='LoopThread')
    # t.start()
    # t.join()
    # # print("thread %s ended."%threading.current_thread().name)

    # t1 = threading.Thread(target=run_thread,args=(4,))
    # t2 = threading.Thread(target=run_thread,args=(5,))
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()
    # print(balance)


    # t1 = threading.Thread(target=for_for)
    # t1.start()
    # t1.join()

    print(multiprocessing.cpu_count())
    ABCD()




