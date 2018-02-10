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
import subprocess

# Pour le serveur HTTP
import SimpleHTTPServer
import SocketServer

# Pour décoder des URL
import urllib

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

# Prémare une chaîne de caractères pour la passer en paramètres via une commande shell
def escapeString(string):
    return '"' + string.replace('\\', '\\\\').replace('"', '\\"').replace('$', '\\$') + '"'

# Traite une demande à l'API en fonction du chemin d'accès
def proceedRequest(path):

    # Lancement d'une recherhce
    if (path.startswith("/api/search/")):

        # Récupère la requête en décodant l'URL
        query = urllib.unquote(path[12:]).decode('utf8')

        # Calcul l'id (md5 de la recherche)
        m = md5.new()
        m.update(query)
        hashid = m.hexdigest()

        # Lance le script de recherche si le résultat n'existe pas déjà
        # Il s'exécute à part, de cette façon il ne bloque pas le serveur
        #os.system('spark-submit "' + root_path + '/back/search.py" ' + escapeString(query) + ' ' + escapeString(hashid))
        #os.spawnl(os.P_NOWAIT, 'spark-submit', [root_path + '/back/search.py', query, hashid])
        if (not os.path.exists(root_path + '/data/results/' + hashid + '.json')):
            subprocess.Popen(["spark-submit", root_path + '/back/search.py', query, hashid], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # On renvoie l'identifiant de la recherche au client pour qu'il puisse récupérer le résultat
        return '{"status":"1","id":"' + hashid + '"}'

    # Demande de résultat d'une recherche
    elif (path.startswith("/api/get-response/")):

        # Récupère l'ID de la requête
        hashid = path[18:]

        # Vérifie si la réponse est prête 
        result_path = root_path + '/data/results/' + hashid + '.json'
        if (not os.path.exists(result_path)):
            return '{"status":"1","id":"' + hashid + '","ready":"0","result":{}}'
        else:
            # On renvoie la réponse
            result = '{}'
            with open(result_path, 'r') as content_file:
                result = content_file.read()
            return '{"status":"1","id":"' + hashid + '","ready":"1","result":' + result + '}'

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
            return self.wfile.write(proceedRequest(self.path))
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
