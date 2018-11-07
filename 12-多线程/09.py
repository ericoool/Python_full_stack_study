import threading
import time

# 参数定义最多几个线程同时使用资源
semaphore = threading.Semaphore(3)

def func():
    if semaphore.acquire():
        print(threading.currentThread().getName() + ' get semaphore')
        time.sleep(2)
        semaphore.release()
        print(threading.currentThread().getName() + ' release semaphore')

# 产生8个func线程,只有三个线程可以同时使用资源.
for i in range(8):
    t1 = threading.Thread(target=func)
    t1.start()