import http.server, socketserver, os
os.chdir(os.path.expanduser("~"))
PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"🌐 Server jalan di: http://127.0.0.1:{PORT}")
    httpd.serve_forever()
