# coding: utf-8

# TweetStats
#
# File          server.py
# Description   Main file of the web server
# Authors       Théophile Walter

# Basics imports
import sys
import os
import atexit

# For the HTTP server
import SimpleHTTPServer
import SocketServer


# Get the parameters
if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 2319


# Set the correct directory
back_path = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.dirname(back_path)
front_path = root_path + '/front'
print ('Going to ' + front_path)
os.chdir(front_path)


# A handler for the HTTP requests
class CustomHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def __init__(self, req, client_addr, server):
        SimpleHTTPServer.SimpleHTTPRequestHandler.__init__(self, req, client_addr, server)
    def do_GET(self):
        # Handle here the request with self.path
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)


# Creates a simple HTTP server
httpd = SocketServer.TCPServer(('localhost', port), CustomHandler)

# Close the socket on exit
# TODO: Does not works all times
def close_socket():
    print ('closing socket.')
    httpd.server_close()

atexit.register(close_socket)

# Run the server
print ('serving at port ' + str(port))
httpd.serve_forever()
