#!/usr/bin/env python
#coding=utf-8
"""
    执行代码前需要安装
    pip install bottle
    pip install websocket-client
    pip install bottle-websocket
"""
# http://www.linuxyw.com/831.html
from bottle import request, Bottle, abort
from geventwebsocket import WebSocketError
from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler
users = set()   # 连接进来的websocket客户端集合
app = Bottle()
users = set()
@app.get('/websocket/')
def handle_websocket():
    wsock = request.environ.get('wsgi.websocket')
    users.add(wsock)
    if not wsock:
        abort(400, 'Expected WebSocket request.')
    while True:
        try:
            message = wsock.receive()
        except WebSocketError:
            break
        print u"现有连接用户：%s" % (len(users))
        if message:
            for user in users:
                try:
                    user.send(message)
                except WebSocketError:
                    print u'某用户已断开连接'
    # 如果有客户端断开，则删除这个断开的websocket
    users.remove(wsock)
server = WSGIServer(("0.0.0.0", 8000), app,handler_class=WebSocketHandler)
server.serve_forever()