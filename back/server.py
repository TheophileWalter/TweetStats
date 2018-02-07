# coding: utf-8

# TweetStats
#
# Fichier       ./back/server.py
# Description   Fichier principal du serveur web
# Auteurs       Théophile Walter

# Imports de base
import sys
import os
import atexit

# Pour le serveur HTTP
import SimpleHTTPServer
import SocketServer


# Récupération des paramètres
if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 2319


# Définition du répertoire courant dans le dossier "front/"
back_path = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.dirname(back_path)
front_path = root_path + '/front'
print ('Going to ' + front_path)
os.chdir(front_path)


# Classe pour traiter manuellement ou automatiquement les requêtes HTTP
class CustomHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def __init__(self, req, client_addr, server):
        SimpleHTTPServer.SimpleHTTPRequestHandler.__init__(self, req, client_addr, server)
    def do_GET(self):
        # Handle here the request with self.path

        if (self.path.startswith("/api/")):
            return self.wfile.write("API")
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)


# Crée un serveur HTTP
httpd = SocketServer.TCPServer(('localhost', port), CustomHandler)

# Ferme le socket à la fin du programme
# TODO: Does not works all times
def close_socket():
    print ('closing socket.')
    httpd.server_close()

atexit.register(close_socket)

# Lance le serveur
print ('serving at port ' + str(port))
httpd.serve_forever()
