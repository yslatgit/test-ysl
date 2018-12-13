import requests

headers = {"cookie":"JSESSIONID=9C24F9A635C1E65673A0F8388D13036E"}
class ABC:
    def __init__(self,name="ysl"):
        self.name = name

    def __str__(self):
        return "姓名是%s"%self.name

# print(ABC())
# a = ABC("YSS")
# print(a)
"""***************************************************************定制类***************************************************************"""
class Screen:
    __slots__ = ('__width','height')

    def __init__(self,width=0,height=0):
        self.__width = width
        self.height = height
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self,width):
        self.__width = width

class D(ABC,Screen):
    pass

class Student:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return "Student object (name:%s)"%self.name

    def __call__(self):
        return "my name is %s"%self.name

    __repr__ = __str__

class Fib:
    def __init__(self):
        self.a,self.b = 0,1

    def __iter__(self):
        return self

    def __next__(self):
        """用于for循环遍历"""
        self.a,self.b = self.b,self.a + self.b
        if self.a > 10:
            raise StopIteration()
        return self.a

    def __getitem__(self, item):
        """可根据下标获取值"""
        a,b = 1,1
        for x in range(item):
            a,b = b,a + b
        return a

    def __getattr__(self, attr):
        """调用没有声明的属性时调用此方法"""
        pass

class Chain:
    def __init__(self,path=''):
        self.__path = path

    def __getattr__(self, attr):
        return Chain('%s/%s'%(self.__path,attr))

    def __str__(self):
        return self.__path

    def users(self,user):
        return Chain('%s/%s'%(self.__path,user))



    __reper__ = __str__

if __name__ == '__main__':
    # a = Screen()
    # a.width = 10
    # print(a.width)
    # print(D.__mro__)
    # s = Student("ysl")
    # print(s())
    # print(s.__repr__())
    # print(Fib()[2])
    # f = Fib()
    # print(f.name)
    # c = Chain()
    # print(c.users("y").s.l)
    # print(c.y.s.l)
    pass