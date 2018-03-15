import http.server, socketserver, os
PORT = 8080
os.chdir(os.path.join(os.path.dirname(__file__), 'webroot'))
print("serving at port", PORT)
try: socketserver.TCPServer(("", PORT), http.server.SimpleHTTPRequestHandler).serve_forever()
except KeyboardInterrupt : print("")
