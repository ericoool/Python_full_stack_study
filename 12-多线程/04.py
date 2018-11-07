import time
import threading

class MyThread(threading.Thread):
    def __init__(self, arg):
        super(MyThread, self).__init__()
        self.arg = arg

    # 必须重写run函数,代表的是真正执行的功能
    def run(self):
        time.sleep(2)
        print("The args for this class is {}".format(self.arg+1))

for i in range(5):
    t = MyThread(i)
    t.start()
    t.join()

print("Main thread is done!!!")