import time, threading

# 新线程执行的代码:
def loop():
    i=0
    while i<10:
       time.sleep(1)
       i=i+1
       print i 


def loop1():
    a=30
    while a<50:
       time.sleep(0.5)
       a=a+1
       print a 







t = threading.Thread(target=loop, name='LoopThread')

t1 = threading.Thread(target=loop1, name='LoopThread1')
t1.start()
t.start()
t.join()
t1.join()
