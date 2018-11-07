import threading
import asyncio

@asyncio.coroutine
def hello():
    print('Hello! (%s)' % threading.currentThread())
    print('Start... (%s)' % threading.currentThread())
    yield from asyncio.sleep(5)
    print('Done... (%s)' % threading.currentThread())
    print('Hello again! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
# 定义两个任务,就是两个协程
tasks = [hello(), hello()]
# asyncio使用wait等待task执行完毕
loop.run_until_complete(asyncio.wait(tasks))
# 关闭消息循环
loop.close()