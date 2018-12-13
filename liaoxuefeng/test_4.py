class A:
    pass
"""***************************************************************StringIO/BttesIO***************************************************************"""

from io import StringIO
f = StringIO()
# for i in range(100000):
#     print(i,"-----",f.write("hello"))
# print(f.write("----"))
print(f.write("world"))
"""调用write方法后指针到了d的位置，只有指针在0（即最开始的位置时才能读取到内容）"""
# print(f.getvalue())
# d = StringIO("hello world")

f.seek(2)
"""通过seek方法移动指针位置"""
print(f.write("--"))
print(f.tell())
f.seek(0)
print(f.readline())