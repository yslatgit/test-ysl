class A:
    pass
"""***************************************************************协程***************************************************************"""
"""生产者消费者"""

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...'%n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...'%n)
        r = c.send(n)
        print('[PRODUCER] Consumer return:%s'%r)
    c.close()

# c = consumer()
# produce(c)
def h():
    """打印语句不会执行"""
    print('To be brave')
    yield 5

def h1():
    """yield原理解密"""
    print('ysl-0')
    yield 5
    print('ysl-1')

if __name__ == '__main__':
    c = h1()
    c.send('123')