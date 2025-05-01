from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers['Content-Length'])
        data = self.rfile.read(length)
        with open("received_pass.json", "wb") as f:
            f.write(data)
        self.send_response(200)
        self.end_headers()

print("Listening on http://0.0.0.0:8000")
server = HTTPServer(('0.0.0.0', 8000), Handler)
try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\n[+] Server stopped by user.")
