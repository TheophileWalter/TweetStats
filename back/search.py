# coding: utf-8

# TweetStats
#
# Fichier       ./back/search.py
# Description   Fichier principal du système de recherche de tweet
# Auteurs       Théophile Walter

# Utilisation :
#   spark-submit search.py query id
# Paramètres :
#   query: Une chaîne de caractères représentant les mots à rechercher
#   id:    L'identifiant unique de la requête (pour l'enregistrement du résultat)

# Permet d'utiliser "print" comme une véritable fonction et non un mot clé
# et donc de la donner en paramètre au lieu d'une fonction lambda
from __future__ import print_function

# Récupère le context spark
from pyspark import SparkContext
sc = SparkContext("local", "TweetStats - Search Engine")

# Imports basiques
import sys
import os
import re # Expressions régulières

# Vérification des paramètres
if (len(sys.argv) < 3):
    print ("Error: Usage \"search.py query id\"")
    exit()

# Définition du répertoire courant dans le dossier "front/"
back_path = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.dirname(back_path)
front_path = root_path + '/front'

# Charge le fichier des tweets dans une RDD
tweets_file = sc.textFile(root_path + '/data/tweets.json')

# Affiche le nombre de lignes dans le fichier
#print (rdd_size(tweets_file))

# Récupération des paramètres
words = re.split('[   ,.;:!?]', sys.argv[1])
hashid = sys.argv[2]

# Vérifie si un des élémentes de "array" est une sous-chaîne de "string"
def search_array_in_string(array, string):
    for e in array:
        if (e in string):
            return True
    return False

# Vérifie si TOUS des élémentes de "array" sont une sous-chaîne de "string"
def search_all_array_in_string(array, string):
    for e in array:
        if (e not in string):
            return False
    return True

# Recherche simple, les tweets contenant au moins un des mots
rdd_one_word = tweets_file.filter(lambda e: search_array_in_string(words, e))

# Recherche les tweets contenant TOUS les mots
rdd_all_words = tweets_file.filter(lambda e: search_all_array_in_string(words, e))

# Ouverture du fichier pour marquer les réponses
out_path = root_path + '/data/results/' + hashid + '_temp.json'
out = open(out_path, 'w') 
out.write('{')
out.write('"countOneOf":"' + str(rdd_one_word.count()) + '",') # Nombre de tweets contenant au moins un des mots
out.write('"countAll":"' + str(rdd_all_words.count()) + '"') # Nombre de tweets contenant tous les mots
out.write('}')
out.close()

# Déplacement du fichier final
os.rename(out_path, root_path + '/data/results/' + hashid + '.json')
