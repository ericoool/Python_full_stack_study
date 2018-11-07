import threading

sum = 0
loopSum = 1000000

def myAdd():
    global sum, loopSum
    for i in range(1, loopSum):
        sum += 1
def myMinu():
    global sum, loopSum
    for i in range(1, loopSum):
        sum -= 1
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