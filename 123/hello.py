# def hello():                                      # 1
#     print("hello world")                              # 2
# print(__name__)                                   # 3
#                                                   # 4
# import sys                                        # 5
# args = sys.argv[1:]                               # 6
# print(args)                                       # 7
# import fileinput                                  # 8
# for line in fileinput.input(inplace=True):        # 9
#     line = line.strip()                               #10
#     num = fileinput.lineno()                          #11
#     print('{:<50}#{:2d}'.format(line,num))            #12
# if __name__ == '__main__':                      #13
import re
def re_split(b):
    some_text = "Alpha,beta,,,lala   Ysl   Gogo"
    a = re.split("[, ]+",some_text,maxsplit=2)
    print(a)

def re_findall():
    text = "D:\Python3\python.exe... 'D:\PyCharm 2016.2.3'\helpers\pydev\pydevd.py??? --multiproc --qt-support"
    #筛选字符串中所有单词的规则
    pat_word = '[a-zA-Z]+'
    print(re.findall(pat_word,text))
    pat_symbol = r"[-\.:?']+"
    print(re.findall(pat_symbol,text))

def re_match_group():
    m = re.match(r'www\.(.*)\..{3}', 'www.python.org')
    print(m.group(0))
    print(m.group(1))
#文件的读取
def open_file():
    f = open("test.txt",'a+')
    f.write("hello world!5\n")
    f.close()
def read_file():
    f = open("test.txt",'r')
    print(f.read())

#图形界面
from tkinter import *
def gui():
    top = Tk()
    # btn = Button()
    Label(text="I'm in the first window!").pack()
    Button(text="Click me",command=read_file).pack()
    for i in range(10):
        Button(text=i).pack()
    # btn.pack()
    # Label(text="I'm in the first window!").pack()
    # btn['text'] = "Click me"
    # btn['command'] = read_file
    second = Toplevel()
    Label(second,text="I'm in the second window!").pack()
    top.bind('<Button-1>',re_split)
    mainloop()

#socket
import socket
def server():
    s = socket.socket()
    host = socket.gethostname()
    port = 1234
    s.bind((host,port))
    s.listen(5)

    while True:
        for i in range (100):
            print("waitting for connection ...")
            c,addr = s.accept()
            print('got connection from :',addr)
            c.send(b'data %d'%i)
            c.close()

import socket
def client():
    s = socket.socket()
    host = socket.gethostname()
    port = 1234
    s.connect((host,port))
    print(s.recv(1024))

#socketserver服务器 同 上面的server
from socketserver import TCPServer,StreamRequestHandler
class Handler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print('got connection from :',addr)
        self.wfile.write(b"Thanks for you connection ...")

server1 = TCPServer(('', 1234), Handler)
server1.serve_forever()



if __name__ == '__main__':
    server1 = TCPServer(('', 1234), Handler)
    server1.serve_forever()