# 协程
- 参考资料:
    - http://python.jobbole.com/86481/
    - http://python.jobbole.com/87310/
    - https://segmentfault.com/a/1190000009781688
# 迭代器
- 可迭代(Iterable): 直接作用于for循环的变量
- 迭代器(Iterator): 不但可以作用于for循环,还可以被next调用
- list是典型的可迭代对象,但不是迭代器
- isinstance
-       # 判断是否可迭代
        from collections import Iterable
        ll = [1,2,3,4,5]
        print(isinstance(ll, Iterable))     -->True
        # 判断是否是迭代器
        from collections import Iterator
        print(isinstance(ll, Iterator))     -->False
- iterable和iterator可以转换
    - 通过iter函数
    -       ll_iter = iter(ll)
            print(isinstance(ll_iter, Iterator))     -->True
# 生成器
- generator: 一边循环一边计算下一个元素的计值/算法
- 需要满足三个条件:
    - 每次调用都产生出for循环需要的下一个元素
    - 如果达到最后一个元素,报出StopIteration异常
    - 可以被next函数调用
- 如何生成以个生成器
    - 直接使用
    -       #直接使用生成器
            l = [x*x for x in range(5)] #放在中括号里是列表
            g = (x*x for x in range(5)) #放在小括号里就是生成器
            print(type(l))  --><class 'list'>
            print(type(g))  --><class 'generator'>
    - 如果函数中包含yield,则这个函数就叫生成器
    - next调用函数,遇到yield返回
    >案例01
    -       # 在函数odd中,yield负责返回
            def odd():
                print("Step 1")
                yield 1
                print("Step 2")
                yield 2
                print("Step 3")
                yield 3
            g = odd()   # 实例化一个生成器.odd是一个object类
            one = next(g)   # 用next调用yield返回的第一个结果
            print(one)      # -->Step 1 -->1
            two = next(g)   # 用next调用yield返回的第二个结果
            print(two)      # -->Step 2 -->2
            three = next(g)   # 用next调用yield返回的第三个结果
            print(three)      # -->Step 3 -->3
    - 可以用for循环调用生成器
        >案例01
        -       def fib(max):           # 斐波那契数列
                n, a, b = 0, 0, 1
                while n < max:
                    yield b         # 用yield每次返回b值
                    a, b = b, a+b
                    n += 1
                return 'Done'
                num = 5
                g_fib = fib(num)
                ge_fib = fib(num)
                for i in range(num):    # 如果循环次数是num+1.则报出异常,返回值是return的Done
                    rst = next(g_fib)
                    print(rst)
                for i in ge_fib:        # 在for循环里直接使用生成器,典型应用
                    print(i)
# 协程
- 历史:
    - 3.4引入协程,用yield实现
    - 3.5引入协程语法
    - 实现协程的比较好的包有asyncio,tornado,gevent
- 定义: 是为非抢占式多任务产生子程序的计算机程序组件,协程允许不同入口点在不同位置暂停或开始执行任务.
- 从技术角度讲,协程就是一个你可以暂停执行的函数,或者把它理解成一个生成器.
- 协程的实现:
    - yield返回
    - send调用
    - >案例02
    -       # 协程代码案例
            def simple_coroutine():
                print('-> start')
                x = yield               # 第一次调用yield返回空
                print('->recived', x)   # 第二次调用,x=yield返回send的参数
            
            # 主线程
            sc = simple_coroutine()
            print(1111)
            next(sc)    # 预激: 可以使用sc.send(None),效果一样
            print(2222)
            sc.send('recall')
- 协程的四个状态:
    - inspect.getgeneratorstate(...)函数确定,该函数返回下述字符串中的一个:
        - GEN_CREATED: 等待开始执行
        - GEN_RUNNING: 解释器正在执行
        - GEN_SUSPENED: 在yield表达式处暂停
        - GEN_CLOSED: 执行结束
    - next预激(prime)
- 协程终止
    - 协程中未处理的异常会向上冒泡,传给next函数或send方法的调用方(即触发协程的对象)
    - 终止协程一种方式: 发送某个哨兵值,让协程退出.内置的None和Ellipsis等常量经常作为哨兵值.
- yield from
    - 调用协程为了得到返回值,协程必须正常终止
    - 生成器正常终止会发出StopIteration异常,异常对象的value属性保存返回值.
    - yield form从内部捕获StopIteration异常
    >案例03
    -       def gen():
                for c in 'AB':
                    yield c
            # list直接用生成器作为参数
            print(list(gen()))
            
            def gen_new():
                yield from('AB')
            print(list(gen_new()))
    - 委派生成器

# asyncio
- python3.4开始引入标准库当中,内置对异步iode支持
- asyncio本身是一个消息循环
- 步骤:
    - 创建消息循环
    - 把协程导入
    - 关闭
    >案例04
    -       import threading
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
    > 案例05
    -       import asyncio

            @asyncio.coroutine
            def wget(host):
                print('wget %s...' % host)
                # 异步请求网络地址
                connect = asyncio.open_connection(host, 80)
                # 注意yield from的用法
                reader, writer = yield from connect
                header = 'GET / HTTP/1.0\r\n Host: %s\r\n\r\n' % host
                writer.write(header.encode('utf-8'))
                yield from writer.drain()
                while True:
                    line = yield from reader.readline()
                    # http协议的换行使用\r\n
                    if line == b'\r\n':
                        break
                    print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
                # Ignore the body, close the socket
                writer.close()
            
            loop = asyncio.get_event_loop()
            tasks = [wget(host) for host in ['www.sina.com.cn', 'www.soho.com', 'www.163.com']]
            loop.run_until_complete((asyncio.wait(tasks)))
            loop.close()
# async and await
- 为了更好的表示异步io
- python3.5引入
- 让协程代码更简洁
- 使用上,可以简单的进行替换
    - 用async 替换 @asyncio.coroutine
    - await 替换 yield from
# aiohttp
- asyncio实现单线程的并发io,在客户端用处不大.
- 在服务器端可以asyncio+coroutine配合,因为http是io操作,远程访问很耗时间.
- asyncio实现了tcp, udp, ssl等协议
- aiohttp是给与asyncio实现的http框架
- pip install aiohttp安装
> 案例06
-       # aiohttp案例
        import asyncio
        from aiohttp import web
        
        async def index(request):
            await asyncio.sleep(0.5)
            return web.Response(body=b'<h1>Index</h1>')
        async def hello(request):
            await asyncio.sleep(0.5)
            text = '<h1>hello, %s!</h1>' % request.match_info['name']
            return web.Response(bady=text.encode('utf-8'))
        async def init(loop):
            app = web.Application(loop=loop)
            app.router.add_route('GET', '/', index)
            app.router.add_route('GET', '/hello/{name}', hello)
            srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
            print('Server started at http://127.0.0.1:8000...')
            return srv
        
        loop = asyncio.get_event_loop()
        loop.run_until_complete(init(loop))
        loop.run_forever()
# concurrent.futures
- python3新增的库
- 类似于其它语言的线程池的概念
- 利用multiprocessing实现真正的并行计算
- 核心原理: 以子进程的形式,并行运行多个python解释器
    - 从而令python程序可以利用多核CPU来提升执行速度
    - 由于子进程与主解释器相分离,所以它们的全局解释器锁也是相互独立的
    - 每个子进程都能完整的使用一个CPU内核
- 使用方法:
    - concurrent.futures.Executor
        - ThreadPoolExecutor 线程池
        - ProcessPoolExrcutor 进程池
        - 执行的时候需要自行选择
    - submit(fn, args, kwargs)
        - fn: 异步执行的函数
        - args, kwargs: 参数
    > 案例07
    -       # concurrent的案例
            from concurrent.futures import ThreadPoolExecutor
            import time
            
            def return_future(msg):
                time.sleep(3)
                return msg
            # 创建一个线程池,设定最多线程池个数
            pool = ThreadPoolExecutor(max_workers=2)
            # 往线程池加入2个task
            f1 = pool.submit(return_future, 'hello')
            f2 = pool.submit(return_future, 'world')
            # 等待执行完毕
            print(f1.done())
            time.sleep(3)
            print(f2.done())
            # 结果
            print(f1.result())
            print(f2.result())
# current中的map函数
- map(fn, *iterables, time=None)
    - 跟map函数类似
    - 函数需要异步执行
    - timeout: 超时时间
    - map跟submit使用一个就可以
    > 案例08
    -       import time,re
            import os,datetime
            from concurrent import futures
            
            data = ['1', '2']
            def wait_on(argument):
                print(argument)
                time.sleep(2)
                return 'ok'
            
            ex = futures.ThreadPoolExecutor(max_workers=2)
            for i in ex.map(wait_on, data):
                print(i)