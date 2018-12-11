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

if __name__ == '__main__':
    # func_5()
    # f = FIFODict(3)
    # f.append('1','a')
    func_6()
