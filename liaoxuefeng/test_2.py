class A:
    pass
"""***************************************************************枚举类***************************************************************"""

from enum import Enum,unique


@unique
class Weenday(Enum):
    """@unique--->可以帮助检查没有重复的值"""
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

@unique
class Gender(Enum):
    Male = 0
    Female = 1

class Student:
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender



if __name__ == '__main__':
    # day1 = Weenday.Mon
    # print(day1.value)
    # print(Weenday.Tue.value)
    # for name,member in Weenday.__members__.items():
    #     print(name ,"--->" ,member.value)
    bart = Student('Bart',Gender.Male)
    if bart.gender == Gender.Male:
        print("测试通过")
    else:
        print("测试失败")