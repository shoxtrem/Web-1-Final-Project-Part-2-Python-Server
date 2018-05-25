# !/usr/bin/python3
# This script generates a simple HTTP server wich can execute cgi scripts
# to run simply go where this file is, make it executable and run
# python3 server.py

from http.server import CGIHTTPRequestHandler, HTTPServer

PORT = 8000

handler = CGIHTTPRequestHandler
handler.cgi_directories = ['/cgi-bin']  # this is the default
server = HTTPServer(('localhost', PORT), handler)
print("Server working on port: ", PORT)
server.serve_forever()
