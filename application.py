import sys
import os 
from http import server


from http.server import BaseHTTPRequestHandler

def read_file(path):
    try:
        with open(path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "File not found"

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        resp_text = f"""<h1>Hello World!</h1>
            <p>Client address: {self.client_address}</p>
            <p>Command: {self.command}</p>
            <p>Path: {self.path}</p>
            <p>Headers: {self.headers}</p>
            <p>Server version: {self.server_version}</p>
            <p>Python version: {sys.version}</p>
            <p>Pre-build content: {read_file('pre-build.txt')}</p>
            <p>Build content: {read_file('build.txt')}</p>
            <p>Post-build content: {read_file('post-build.txt')}</p>
            <p>Pre-run content: {read_file('pre-run.txt')}</p>
        """
        resp_data = resp_text.encode('utf8')
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", len(resp_data))
        self.end_headers()
        self.wfile.write(resp_data)

if __name__ == "__main__":
    serv = server.HTTPServer(('0.0.0.0', 8000), RequestHandler)
    serv.serve_forever()