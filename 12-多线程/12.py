import multiprocessing
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