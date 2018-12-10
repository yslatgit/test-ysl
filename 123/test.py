#递归 factorial pow
def factorail(n):
    result = n
    for i in range(1,n):
        result *=i
    return result

def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n-1)

def power(x,n):
    result =1
    for i in range(n):
        result *=x
    return result

def poww(x,n):
    if x == 1 or n == 0:
        return  1
    else:
        return x * poww(x,n-1)

lala = ("SPAN",2.50)
def get_price(object):
    if isinstance(object,tuple):
        return object[1]
    else:
        pass

class OpenObiect():
    # name = None
    def set_name(self,name):
        self.name = name

    def get_name(self):
        return self.name
#继承
class Filter():
    def init(self):
        self.block = []

    def filter(self,sequence):
        return [x for x in sequence if x not in self.block]

class SAMPFilter(Filter):
    def init(self):
        self.block = ['SPAM']


#多继承
class Calculator:
    def calculator(self,ex):
        self.value = eval(ex)

class Talker:
    def talk(self):
        print("my vlaue is %s"%self.value)

class TalkingCalculator(Calculator, Talker):
    pass

#抽象类
from abc import ABC, abstractmethod
class Talk(ABC):
    @abstractmethod
    def talk(self):
        pass

class King(Talk):
    def talk(self):
        print("123")

#异常
class MuffledCalculator:
    muffled = False
    def calc(self,expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print("Division by zero is illeagl")
            else:
                raise

class FooBar:
    #构造方法（初始化方法）
    def __init__(self,value = 12):
        self.age = value
    #析构方法（创建的对象在销毁之前调用）
    def __del__(self):
        print("bey")

class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print("Aaaaaa")
            self.hungry = False
        else:
            print("No Thanks")
class SongBird(Bird):
    def __init__(self):
        # super().__init__()
        Bird.__init__(self)
        self.sound = "huanghun"
    def song(self):
        print(self.sound)

def check_index(key):
    if not isinstance(key,int):
        raise TypeError
    if key < 0:
        raise IndexError

class ArithmeticSequence:
    #初始化这个算数序列
    def __init__(self,start=0,step=1):
        self.start = start
        self.step = step
        self.changed = {}

    #从算数序列中获取一个元素
    def __getitem__(self, key):
        check_index(key)
        try:
            return self.changed[key]
        except KeyError:
            return self.start + key * self.step

    #修改算数序列中的元素
    def __setitem__(self, key, value):
        check_index(key)
        self.changed[key] = value

#一个带计数器的列表
class CounterList(list):
    def __init__(self,*args):
        super().__init__(*args)
        self.counter = 0

    def __getitem__(self, index):
        self.counter += 1
        return super(CounterList,self).__getitem__(index)

#__setattr__,__getattr__魔法方法
class Rectangle:
    def __init__(self):
        # print("1")
        self.width = 0
        self.height = 0
        # self.ysl = "ysl"

    # def set_size(self,size):
    #     self.width,self.height = size
    #
    # def get_size(self):
    #     return self.width,self.height
    #
    # size = property(get_size,set_size)
    def __setattr__(self, key, value):
        """试图给属性赋值时自动调用"""
        print("setattr")
        if key == "size":
            self.width,self.height = value
        else:
            self.__dict__[key] = value

    def __getattr__(self, item):
        """获取对象中没有的属性时调用"""
        print("getattr")
        if item == "size":
            return self.width,self.height
        else:
            raise AttributeError

#迭代器-->斐波那契数列
class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __next__(self):
        print("__next__")
        self.a ,self.b = self.b ,self.a + self.b
        return self.a

    def __iter__(self):
        print("__iter__")
        return self

#自定义列表迭代器
class TestIterator:
    value = 0
    def __next__(self):
        if self.value <= 20:
            self.value += 2
        else:
            raise StopIteration
        return self.value

    def __iter__(self):
        return self

#生成器函数
# nested = [[1,2],[3,4],[5]]
def flatten(nested):
    try:
        try:
            nested + ''
        except TypeError:
            pass
        else:
            raise TypeError
        for sublist in nested:
            for i in flatten(sublist):
                yield i
                print("1")
    except TypeError:
        yield nested

#八皇后问题
def conflict(state,nextX):
    """冲突函数"""
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i] - nextX) in (0,nextY - i):
            return True
    return False

def queens(num,state):
    if len(state) == num - 1:
        for pos in range(num):
            if not conflict(state,pos):
                yield pos

def queens_s(num=8,state=()):
    for pos in range(num):
        if not conflict(state,pos):
            if len(state ) == num -1:
                yield (pos,)
            else:
                for result in queens_s(num,state + (pos,)):
                    yield (pos,) + result

def prettyprint(position):
    def line(pos,length = len(position)):
        return "." * (pos) + "X" + "." * (length - pos -1)
    for pos in position:
        print(line(pos),pos)

def aaa(a):
    # try:
    #     1 / 0
    # except ZeroDivisionError:
    #     raise ValueError

    # try:
    #     x = int(input('Enter the first number: '))
    #     y = int(input('Enter the second number: '))
    #     print(x / y)
    # except (ZeroDivisionError,ValueError, TypeError, NameError):
    #     print('Your numbers were bogus ...')

    # raise ZeroDivisionError
    try:
        if a > 10:
            return 1
    except:
        print("999")

print("sdfasdfsdf")
import socket
def client():
    s = socket.socket()
    host = socket.gethostname()
    port = 1234
    s.connect((host,port))
    print(s.recv(1024))

if __name__ == '__main__':
    # o = OpenObiect()
    # o.set_name("ysl")
    # # o1 = OpenObiect()
    # print(o.get_name())
    # print(o.name)
    # # print(o1.get_name())
    # f = Filter()
    # f.init()
    # print(f.filter([1,2,3]))
    # s = SAMPFilter()
    # s.init()
    # print(s.filter(['SPAM', 'SPAM', 'SPAM', 'SPAM', 'eggs', 'bacon', 'SPAM']))
    # t = TalkingCalculator()
    # t.calculator("1 + 2 * 3")
    # t.talk()
    # print(TalkingCalculator.__bases__)
    # k = King()
    # k.talk()
    # ca = MuffledCalculator()
    # ca.muffled = True
    # ca.calc("10 / 0")

    # aaa()

    # f = FooBar(15)
    # print(f.age)
    # b = Bird()
    # b.eat()
    # b.eat()
    # s = SongBird()
    # s.song()
    # s.eat()
    # ar = ArithmeticSequence(1,2)
    # print(ar[-2])
    # ar[4] = 19
    # print(ar[4],ar[2])
    # cl = CounterList(range(10))
    # cl.reverse()
    # print(cl[4] + cl[5] + cl[6])
    # # print(cl)
    # print(cl.counter)
    # re = Rectangle()
    # re.width = 10
    # re.height = 20
    # print(re.size)
    # re.aaa = (100,150)
    # print(re.bbb)
    # print(re.ysl)
    # fibs = Fibs()
    # for i in fibs:
    #     if i < 100:
    #         print(i)
    #     else:
    #         break
    # te = TestIterator()
    # print(te)
    # for num in flatten(nested):
    #     print(num)
    # print( list(flatten([[[1], 2], 3, 4, [5, [6, 7]], 8])))
    # print(list(queens_s(4)))
    # import random
    #
    # prettyprint(random.choice(list(queens_s(4))))
    import hello
    # client()
