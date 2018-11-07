# 环境
- xubuntu
- anaconda
- pycharm
- python
- https://www.cnblogs.com/jokerbj/p/7460260.html
- http://www.dabeaz.com/python/UnderstandingGIL.pdf

# 多线程 VS 多进程
- 程序: 一堆代码以文件形式存入一个文档
- 进程: 程序运行的一个状态
    - 包含地址空间,内存,数据栈等
    - 每个进程由自己完全独立的运行环境,多进程共享数据是一个问题
- 线程: 一个进程的独立运行片段,一个进程可以有多个线程
    - 轻量化的进程
    - 一个进程的多个线程之间共享数据和上下文运行环境
    - 共享互斥问题
- 全局解释器锁(GIL)
    - Pyhton代码的执行是由python虚拟机进行控制
    - 在主循环中只能有一个控制线程在执行

- Python包
    - thread: 在python3中改为_thread
    - threading: 通行的包
    - > 案例01: 使用_thread
    
    -       import time
            import _thread as thread

            def loop1():
                print('Start loop1 at: ', time.ctime())
                time.sleep(4)
                print('End loop1 at: ', time.ctime())

            def loop2():
                print('Start loop2 at: ', time.ctime())
                time.sleep(2)
                print('End loop2 at: ', time.ctime())

            def main():
                print('Starting at: ', time.ctime())
                thread.start_new_thread(loop1, ())
                thread.start_new_thread(loop2, ())
                print('All done at: ', time.ctime())

            if __name__ == '__main__':
                main()
                while True:
                    time.sleep(1)
    
- threading的使用
    - 直接利用threading.Thread生成Thread实例
        1. t = threading.Thread(target=xxx, args=(xxx,))注意参数应该是元组形式
        2. t.start(): 启动多线程
        3. t.join(): 等待多线程执行完成
        4. > 案例02
        -       import time
                import threading
                
                def loop1(in1):
                    print('Start loop1 at: ', time.ctime())
                    print("我是参数 ", in1)
                    time.sleep(4)
                    print('End loop1 at: ', time.ctime())
                
                def loop2(in1, in2):
                    print('Start loop2 at: ', time.ctime())
                    print("我是参数 ", in1, "和参数 ", in2)
                    time.sleep(2)
                    print('End loop2 at: ', time.ctime())
                
                def main():
                    print('Starting at: ', time.ctime())
                    t1 = threading.Thread(target=loop1, args=("二哈",))
                    t1.start()
                    t2 = threading.Thread(target=loop2, args=("二哈", "货货"))
                    t2.start()
                
                    t1.join()   # 等待多线程完成后再执行之后语句.
                    t2.join()
                
                    print('All done at: ', time.ctime())
                
                if __name__ == '__main__':
                    main()
        5. 守护线程-daemon
            - 如果再程序中将子线程设置成守护线程,则子线程会在主线程结束时自动退出
            - 一般认为,守护线程不重要,或则不允许离开主线程独立运行
            - 守护线程案例能否有效果跟环境有关
            - > 案例03: 子线程设为守护线程daemon
            -       import time
                    import threading
                    
                    def func():
                        print("Start func")
                        time.sleep(2)
                        print("End func")
                    
                    print("Main thrad")
                    
                    t1 = threading.Thread(target=func, args=())
                    # 守护线程必须在子线程启动之前设置,否则无效.
                    t1.setDaemon(True)  # 这两个用法同样的效果
                    t1.daemon = True    # 设置守护线程后,子线程的最后语句print("End func")在主线程结束后不执行
                    t1.start()
                    
                    time.sleep(1)
                    print("Main thread end")
        6. 线程常用属性
            - threading.currentThread: 返回当前线程变量
            - threading.enumerate: 返回一个包含正在运行的线程list
            - threading.activeCount: 返回正在运行的线程数
            - thr.setName: 给线程设置名字
            - thr.getName: 得到线程的名字
    - 直接继承自threading.Thread
        - 重写run函数,把子线程写到run函数里
        - 类实例可以直接运行
        - > 案例04
        -       import time
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
        - > 案例05-多线程实用代码
        -       import threading
                from time import sleep, ctime
                
                #loop = [4, 2]
                class ThreadFunc:
                    def __init__(self, name):
                        self.name = name
                    def loop(self, nloop, nsec):
                        '''
                
                        :param nloop: loop函数的名称
                        :param nsec: 系统休眠时间
                        :return:
                        '''
                        print('Start loop', nloop, 'at', ctime())
                        sleep(nsec)
                        print('Done loop', nloop, 'at', ctime())
                
                def main():
                    print('Staring at', ctime())
                    # ThreadFunc("loop").loop 跟以下两个语句相等
                    # t = ThreadFunc("loop")
                    # t.loop
                    # 以下t1和t2的定义方式相等
                    t = ThreadFunc("loop")
                    t1 = threading.Thread(target=t.loop, args=("LOOP1", 4))
                    # 下面这种写法更工业化一点
                    t2 = threading.Thread(target=ThreadFunc('loop').loop, args=("LOOP2", 2))
                
                    t1.start()
                    t2.start()
                
                    t1.join()
                    t2.join()
                
                    print("All done at:", ctime())
                
                if __name__ == '__main__':
                    main()
- 共享变量
    - 当多个线程同时访问一个变量时,会产生共享变量的问题
    - 案例06
    - 解决方法: 锁,信号灯
        - 锁(Lock):
            - 是一个标准,表示一个线程正在占用一些资源
            - 上锁-->释放锁
            - > 案例07: 安全锁Lock
            -       import threading

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
            - 锁谁: 那个资源需要多线程共享,锁那个
            - 理解锁: 锁其实可以理解为一个令牌
    - 线程安全问题:
        - 如果一个资源/变量,它对于多线程来讲,不用加锁也不会引起任何问题.
        - 线程不安全的变量类型: list,set,dict
        - 线程安全的变量类型: queue
    - 生产者消费问题:
        - 一个模型,可以用来搭建消息队列
        - queue是用来存放变量的数据结构,特点是先进先出,内部元素排队,可以理解成一个特殊的list
        - > 案例08: 队列queue
        -       import threading
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
    - 锁死问题: 两把锁分别被两个线程申请,注意释放时机
    - 申请锁的等待时间: ``lock.acquire(timeout=0)``
    - semphore
        - 允许一个资源最多有几个线程同时使用
        - > 案例09: semphore
        -       import threading
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
    - threading.Timer
        - 利用多线程,在指定时间后启动一个功能
    -       # 设定6秒后开始执行func函数
            t = threading.Timer(6, func)
    - 可重入锁
        - 一个锁,可以被一个线程多次申请
        - 主要解决递归调用的时候,需要反复申请锁的情况
        - > 案例10: threading.RLock()
        -       import threading
                import time
                
                class MyThread(threading.Thread):
                    def run(self):
                        global num
                        time.sleep(1)
                        if mutex.acquire(1):
                            num += 1
                            msg = self.name + ' set num to ' + str(num)
                            print(msg)
                            mutex.acquire()
                            mutex.release()
                            mutex.release()
                num = 0
                mutex = threading.RLock()
                
                def testTh():
                    for i in range(5):
                        t = MyThread()
                        t.start()
                
                if __name__ == '__main__':
                    testTh()

# 线程替代方案
- subprocess
    - 完全跳过线程,使用进程
    - 是派生进程的主要替代方案
    - python2.4后引入
- multiprocessing
    - 使用threading接口派生,使用子进程
    - 允许为多核或者多cpu派生进程,接口跟threading非常相似
    - python2.6
- concurrent.futures
    - 新的异步执行模块
    - 任务级别的操作
    - python3.2后引入
## 多进程
- 进程间通讯(InterprocessCommunication, IPC)
- 进程间无任何共享状态
- 进程的创建
    - > 案例11:
    -       import multiprocessing
            import time
            
            class ClockProcess(multiprocessing.Process):
                def __init__(self, interval):
                    super().__init__()
                    self.interval = interval
            
                def run(self):
                    while True:
                        print("The time is %s" % time.ctime())
                        time.sleep(self.interval)
            
            if __name__ == '__main__':
                p = ClockProcess(3)
                p.start()
- 在os模块中可以查看进程的id
    - os.getppid()  查看父进程
    - os.getpid()   查看本进程
- 生产者消费者模型
    - JoinableQueue
    - 哨兵值
    - > 案例12:
    -       import multiprocessing
            import time
            
            def comsumer(output_q):
                print("Into consumer: ", time.ctime())
                while True:
                    item = output_q.get()    # 不断的从队列中取出值
                    if item is None:    # 判断哨兵值来中断循环
                        print(output_q.task_done())     # 发出信号通知任务完成,返回的是哨兵值None
                        break
                    print("pull", item, "out of q")     # 此处替换为进程要实现的功能
                print("Out of consumer:", time.ctime())
            
            def producer(sequence, input_q):
                print("Into procuder: ", time.ctime())
                for item in sequence:   # 将列表中的值一个个放入队列中
                    input_q.put(item)
                    print("put", item, "into q")
                print("Out of procuder: ", time.ctime())
            
            # 建立消费者进程
            if __name__ == "__main__":
                q = multiprocessing.JoinableQueue()  # 实例化一个多进程队列
                #q = multiprocessing.Queue()  # 同上,但这个类里面没有task_done()方法
                cons_p = multiprocessing.Process(target=comsumer, args=(q,))    # 建立消费者进程,参数为队列q
                cons_p.start()      # 运行消费者进程
            
                sequence = [1,2,3,4,5]    # 这是要发送给生产者的值
                producer(sequence, q)   # 运行生产者,将sequence的值传到队列q中
            
                q.put(None)     # 在队列q里放入哨兵值None,如果有几个消费者进程,则要提供相应数量的哨兵值
                # 让主进程等待消费者进程结束
                cons_p.join()