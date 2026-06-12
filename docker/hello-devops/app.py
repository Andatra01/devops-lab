from http.server import HTTPServer, BaseHTTPRequestHandler
import os

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello World!')

port = int(os.environ.get('PORT', 8000))
print(f'Starting on port {port}')
HTTPServer(('', port), Handler).serve_forever()
# new comment
