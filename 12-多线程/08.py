# encoding=utf-8
import threading
import time
import queue

class Producer(threading.Thread):
    def run(self):
        global queue
        count = 0
        while True:
            # qsize返回queue内容长度
            if queue.qsize() < 10:
                for i in range(10):
                    count += 1
                    msg = self.name + '生成产品' + str(count)
                    # put是往queue中放入一个值
                    queue.put(msg)
                    print(msg)
            time.sleep(0.5)

class Comsumer(threading.Thread):
    def __init__(self):
        super().__init__()
    def run(self):
        global queue
        while True:
            # qsize返回queue内容长度
            if queue.qsize() > 5:
                for i in range(3):
                    # get是从queue中取出一个值
                    msg = self.name + '消费了' + queue.get()
                    print(msg)
            time.sleep(1)

if __name__ == '__main__':
    queue = queue.Queue()

    for i in range(3):
        queue.put('初始产品'+str(i))
    for i in range(2):
        p = Producer()
        p.start()
    for i in range(5):
        c = Comsumer()
        c.start()
