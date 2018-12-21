"""***************************************************************/asyncio/***************************************************************"""
import asyncio

@asyncio.coroutine
def hello():
    print("Hello World!")
    #异步调用asynico.sleep(1)
    r = yield  from asyncio.sleep(1)
    print("Hello again!")

def t1():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(hello())
    loop.close()


import threading

@asyncio.coroutine
def hello_2():
    print('Hello World! （%s）' %threading.currentThread())
    yield  from asyncio.sleep(1)
    print('Hello again! （%s）' %threading.currentThread())

def t2():
    loop = asyncio.get_event_loop()
    tasks = [hello_2(),hello_2()]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

@asyncio.coroutine
def wegt(host):
    print('wegt %s ...'%host)
    connect = asyncio.open_connection(host,80)
    reader,writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' %host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield  from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    writer.close()

def t3():
    loop = asyncio.get_event_loop()
    tasks = [wegt(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

if __name__ == '__main__':
    t3()