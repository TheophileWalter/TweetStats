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
import md5

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
print ('Moving working directory to ' + front_path)
os.chdir(front_path)

# Traite une demande à l'API en fonction du chemin d'accès
def preceedRequest(path):

    # Lancement d'une recherhce
    if (path.startswith("/api/search/")):

        #TODO: Lancer le script de recherche

        # Calcul l'id (md5 de la recherche)
        m = md5.new()
        m.update(path[12:])
        hashid = m.hexdigest()
        return '{"status":"1","id":"' + hashid + '"}'

    # Demande de résultat d'une recherche
    elif (path.startswith("/api/get-response/")):

        # TODO: Vérifier si la réponse est prête et la retourner
        hashid = path[18:]
        return '{"status":"1","id":"' + hashid + '","result":{}}'

    # Erreur
    else:
        return '{"status":"0","error":"Unknown API action!"}'

# Classe pour traiter manuellement ou automatiquement les requêtes HTTP
class CustomHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def __init__(self, req, client_addr, server):
        SimpleHTTPServer.SimpleHTTPRequestHandler.__init__(self, req, client_addr, server)

    def do_GET(self):
        # Récupère les requêtes qui concernent l'API pour les traiter manuellement
        if (self.path.startswith("/api/")):
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            return self.wfile.write(preceedRequest(self.path))
        # Si la requête concerne un fichier classique, on laisse faire le serveur
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
