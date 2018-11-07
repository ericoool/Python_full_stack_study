import threading

sum = 0
loopSum = 1000000
# 创建一个锁的实例
lock = threading.Lock()

def myAdd():
    global sum, loopSum
    for i in range(1, loopSum):
        # 上锁
        lock.acquire()
        sum += 1
        # 释放锁
        lock.release()
def myMinu():
    global sum, loopSum
    for i in range(1, loopSum):
        # 上锁
        lock.acquire()
        sum -= 1
        # 释放锁
        lock.release()
if __name__ == '__main__':
    print("Starting ...{}".format(sum))
    # 开始多线程,产生共享变量冲突,每次执行最后sum值不确定
    t1 = threading.Thread(target=myAdd, args=())
    t2 = threading.Thread(target=myMinu, args=())

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("Done ...{}".format(sum))