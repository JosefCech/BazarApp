import http.server
import socketserver

import punq

from src.handlers.web_handler import WebHandler

PORT = 8080
container = None


def set_dependency(container):
    container.register(WebHandler, WebHandler, template_prefix="C:/Work/Private/Private/BazarApp-server/")
    return container


class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        global container
        if not container:
            container = punq.Container()
            container = set_dependency(container)
        handler: WebHandler = container.resolve(WebHandler)
       # print(handler.form())
        self.send_response(200)
        self.end_headers()
        self.wfile.write(str(handler.store_item_form()).encode())


Handler = SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
