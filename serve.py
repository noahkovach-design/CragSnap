import os, http.server, socketserver
os.chdir(os.path.dirname(os.path.abspath(__file__)))
PORT = 8765
http.server.SimpleHTTPRequestHandler.protocol_version = "HTTP/1.0"
with socketserver.TCPServer(("127.0.0.1", PORT), http.server.SimpleHTTPRequestHandler) as httpd:
    httpd.serve_forever()
