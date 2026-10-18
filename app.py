import http.server
import socketserver

def add(a, b):
    return a + b

def is_service_healthy():
    return True

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        message = f"🚀 CI/CD Pipeline Successful! Service is running on Kubernetes. 2 + 3 = {add(2, 3)}"
        self.wfile.write(message.encode('utf-8'))

if __name__ == "__main__":
    print("Starting web server on port 8000...")
    with socketserver.TCPServer(("", 8000), Handler) as httpd:
        httpd.serve_forever()
