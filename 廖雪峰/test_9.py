import socket,time

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# s.connect(('www.sina.com.cn',80))
s.connect(('10.0.12.88',6000))

# s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# print(1)
# s.send(b'123')
# buffer = []

while True:
    # d = s.recv(1024)
    # if d:
    #     buffer.append(d)
    # else:
    #     break
    print(1)
    s.send(b'123')
    print(2)
    content = s.recv(1024).decode('gbk')
    if "杨" in content:
        print("哈哈哈")
    print(3)
    # time.sleep(1)

# data = b''.join(buffer)

s.close()

# print(data)
# header,html = data.split(b'\r\n\r\n',1)
# print(header.decode('utf-8'))
#
# with open('sina.html','wb') as f:
#     f.write(html)