import http.server
import socketserver
from urllib.parse import urlparse
from urllib.parse import parse_qs
from utils import get_word, get_letters
import json
import numpy
import cv2

class HttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'classifier/dist/classifier/index.html'
        else:
            self.path = 'classifier/dist/classifier/' + self.path
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        data = self.rfile.read(int(self.headers['content-length']))
        image = cv2.imdecode(numpy.fromstring(data, numpy.uint8), cv2.IMREAD_UNCHANGED)
        letter, image = get_letters(image)
        word = get_word(letter)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(json.dumps({'label': word}).encode())
        return

PORT = 8000
my_server = socketserver.TCPServer(("", PORT), HttpRequestHandler)

# Star the server
my_server.serve_forever()
