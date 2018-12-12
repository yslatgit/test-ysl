class A:
    pass

"""***************************************************************常用模块***************************************************************"""
"""datetime"""
from datetime import datetime
import time
# print(datetime.now().hour)
# print(datetime.now().minute)

def func_1():
    hour = input("输入时间（例：16:7）：")
    print(hour)
    print(type(hour.split(":")[0]))
    while True:
        time.sleep(2)
        if datetime.now().hour == int(hour.split(":")[0]) and datetime.now().minute == int(hour.split(":")[1]):
            print("ysl ---- ysl")
            break

"""collections"""
from collections import namedtuple
"""namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。"""
def func_2():
    """用tuple来表示坐标"""
    Point = namedtuple('Point',['x','y'])
    p = Point(1,2)
    print(p.x)
    print(p.y)

"""deque 实现了lsit的append()和pop()还支持appendleft().popleft()------>双向列表
                                                        list -------->单向列表
"""
from collections import deque
def func_3():
    q = deque(['a','b','c'])
    q.append('x')
    q.appendleft("y")
    q.pop()
    q.popleft()
    print(q)
"""defaultdict"""
from collections import defaultdict
"""使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict"""
def func_5():
    dd = defaultdict(lambda :'N/A')
    dd['k1'] = 'a'
    print(dd['k1'])
    print(dd['k2'])

"""OrderedDict"""

from collections import OrderedDict
class FIFODict(OrderedDict):
    def __init__(self,capacity):
        super(FIFODict,self).__init__()
        self.capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self.capacity:
            last = self.popitem(last=False)
            print('remove:',last)
        if containsKey:
            del self[key]
            print('set:',(key,value))
        else:
            print('add:',(key,value))
        OrderedDict.__setitem__(self,key,value)

"""counter"""
from collections import Counter
def func_6():
    c = Counter()
    list = ["A","A","A","B","B","C"]
    for ch in list:
        c[ch] = c[ch] + 1
    print(c)

"""hashlib"""
import hashlib
def func_7():
    md5_1 = hashlib.md5()
    md5_2 = hashlib.md5()
    md5_1.update('123456'.encode('utf-8'))
    md5_2.update('ysl2'.encode('utf-8'))
    print(md5_1.hexdigest())
    print(len(md5_2.hexdigest()))

"""contextlib"""
from contextlib import contextmanager
#很多时候我们希望在某段代码前后自动执行特定的代码
# 代码的执行顺序是：
# 1.with语句首先执行yield之前的语句，因此打印出<h1>；
# 2.yield调用会执行with语句内部的所有语句，因此打印出hello和world；
# 3.最后执行yield之后的语句，打印出</h1>
@contextmanager
def tag(name):
    print("<%s>"%name)
    yield
    print("</%s>"%name)
def func_8():
    with tag("h1"):
        print("hello")
        print("ysl")

"""urllib"""
from urllib import request
import json
#decode-->字节转字符   encode-->字符转字节
def func_9(url):
    with request.urlopen(url) as f:
        context = f.read()
        context = json.loads(context.decode('utf-8'))
    print(context)

"""HTMLParser"""
from html.parser import HTMLParser
import re
#解析网页
class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.j_time = False
        self.j_title = False
        self.j_location = False
        self.j_year = False
        self.all_info = []

    def handle_starttag(self, tag, attrs):
        if tag == 'span' and ('class','say-no-more') in attrs:
            self.j_year = True
        elif tag == 'span' and ('class','event-location') in attrs:
            self.j_location = True
        elif tag == 'h3' and ('class','event-title') in attrs:
            self.j_title = True
        elif tag == 'time':
            self.j_time = True

    def handle_data(self, data):
        if self.j_year is True:
            if re.match(r'[0-9]',data.strip()):
                self.all_info.append(dict(年份=data))
        elif self.j_title is True:
            self.all_info.append(dict(主题=data))
        elif self.j_location is True:
            self.all_info.append(dict(位置=data))
        elif self.j_time is True:
            self.all_info.append(dict(时间=data))

def deal(content):
    cope = MyHTMLParser()
    cope.feed(content)
    count = 0
    for i in cope.all_info:
        count+= 1
        print(i)
        if count % 4 == 0:
            print("---------------------------------------")


if __name__ == '__main__':
    # func_5()
    # f = FIFODict(3)
    # f.append('1','a')
    # func_9("https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json")
    # print(type("s".encode()))
    # print(type(b't'.decode('utf-8')))
    # pass
    with request.urlopen("https://www.python.org/events/python-events/") as f:
        Data = f.read()
    print(deal(Data.decode('utf-8')))