from wsgiref.simple_server import make_server

def application(environ,start_response):
    start_response('200 OK',[('Content-Type', 'text/html')])
    return[b'<h1>Hello YSL</h1>']

def application2(environ,start_response):
    start_response('200 OK',[('Content-Type','text/html')])
    body = '<h1>Hello,%s</h1>'%(environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]
def test_server():
    #创建一个服务器
    httpd = make_server('',8000,application2)
    print('Server HTTP on port 8000 ....')
    #开始监听HTTP请求
    httpd.serve_forever()

if __name__ == '__main__':
    test_server()