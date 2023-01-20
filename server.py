import http.server
import socketserver

import requests

import mysql


class handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self) -> None:
        if self.path == '/calibracao':
            self.path = 'testado'
        return http.server.SimpleHTTPRequestHandler(self)


server = socketserver.TCPServer(('', 5000), handler)

server.serve_forever()

