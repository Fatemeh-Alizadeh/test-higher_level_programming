import json
from http.server import HTTPServer, BaseHTTPRequestHandler

class requestHendler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!".encode('utf-8'))

        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            dic = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(dic).encode())

        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            dic = {"version": "1.0", "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(dic).encode())

        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write("OK".encode('utf-8'))

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.send_error(404, message="Endpoint not found")



server = HTTPServer(('', 8000), requestHendler)
print('Server running on port 8000')
server.serve_forever()
server.server_close()