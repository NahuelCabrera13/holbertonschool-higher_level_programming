import http.server
import json
import socketserver

PORT = 8000

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/palin")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":m    
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            json_data = json.dumps(data)
            self.wfile.write(json_data.encode("utf-8"))

        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'OK')

        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            info_data = {"version": "1.0", "description": "A simple API built with http.server"}
            json_info_data = json.dumps(info_data)
            self.wfile.write(json_info_data.encode("utf-8"))

        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("el servidor esta abierto")
    httpd.serve_forever()
