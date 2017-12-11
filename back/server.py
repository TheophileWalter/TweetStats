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
print 'Going to ', front_path
os.chdir(front_path)

# Creates a simple HTTP server
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(('localhost', port), Handler)

# Close the socket on exit
def close_socket():
    print 'closing socket.'
    httpd.server_close()

atexit.register(close_socket)

# Run the server
print 'serving at port', port
httpd.serve_forever()
