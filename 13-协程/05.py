import asyncio

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