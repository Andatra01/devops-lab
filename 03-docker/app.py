from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/health':
            body = json.dump({"status": "ok"}).encode()
        else:
            body = b"Hello World!"
        self.send_response(200)
        self.end_headers()
        self.wfile.write(body)

port = 8000
HTTPServer(('', port), Handler).serve_forever()
