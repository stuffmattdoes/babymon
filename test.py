from http import server
import socketserver

PORT = 8080
Handler = server.SimpleHTTPRequestHandler

with socketserver.TCPServer(('', PORT), Handler) as httpd:
    print('serving at port ', PORT)
    httpd.serve_forever()