#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

from icecream import ic
from gevent.pywsgi import WSGIHandler, WSGIServer


PORT = 9283


def app(env, startResponse):
    path = env['PATH_INFO']
    if path.endswith('.png'):
        startResponse('200 OK', [('Content-Type', 'image/png')])
        with open('p.png', 'rb') as f:
            raw = f.read()
        return [raw]
    else:
        startResponse('200 OK', [('Content-Type', 'text/plain')])
        return [path.encode('utf8')]


class TcpAwareWSGIServer(WSGIServer):
    def handle(self, sock, addr):
        ic('new socket!', sock)
        super().handle(sock, addr)


def main():
    server = TcpAwareWSGIServer(('0.0.0.0', PORT), app)
    print(f'Listening on {PORT}...')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass  # gobble ctrl-c SIGINT


if __name__ == '__main__':
    main()
