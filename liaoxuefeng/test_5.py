import os,json
print(os.name)
print(os.listdir("./"))

import pickle
d = dict(name = "ysl",score = 88)
a = pickle.dumps(d)
with open("pickle.txt","wb") as f:
    f.write(a)
"""序列化：输出真正的中文需要指定ensure_ascii=False"""
ff = open("pickle.txt","rb")
ff = ff.read()
dd = pickle.loads(ff)
print(dd)


class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age


def class_to_json(std):
    return{
        "name":std.name,
        "age":std.age
    }

if __name__ == '__main__':
    s = Student("杨松林",20)
    print(json.dumps(s,default=class_to_json,ensure_ascii=False))