from http.server import BaseHTTPRequestHandler, HTTPServer

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(b'Hello, World!\n')


def run(server_class=HTTPServer, handler_class=HelloHandler):
    server_address = ('0.0.0.0', 8000)
    httpd = server_class(server_address, handler_class)
    print(f'Serving on http://{server_address[0]}:{server_address[1]}')
    httpd.serve_forever()


if __name__ == '__main__':
    run()