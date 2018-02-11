# coding: utf-8

# TweetStats
#
# Fichier       ./back/search.py
# Description   Fichier principal du système de recherche de tweet
# Auteurs       Théophile Walter, Alexis Marembert

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
import json
import datetime

# Vérification des paramètres
if (len(sys.argv) < 3):
    print ("Error: Usage \"search.py query id\"")
    exit()

# Définition du répertoire courant dans le dossier "front/"
back_path = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.dirname(back_path)
front_path = root_path + '/front'

# Charge le fichier des tweets dans une RDD et décode le JSON
tweets_file = sc.textFile(root_path + '/data/tweets.json').map(lambda line: json.loads(line))

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

# Echape une chaîne de caractères pour du JSON
def escape_string(string):
    return string.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')


# Recherche simple, les tweets contenant au moins un des mots
rdd_one_word = tweets_file.filter(lambda e: search_array_in_string(words, e['text']))

# Recherche les tweets contenant TOUS les mots
rdd_all_words = tweets_file.filter(lambda e: search_all_array_in_string(words, e['text']))

# Récupère les coordonnées
rdd_coords = rdd_one_word.filter(lambda e: e['coordinates'] != None and e['coordinates']['type'] == 'Point').map(lambda e: e['coordinates']['coordinates'])

# Compte les mots les plus utilisés
word_count = rdd_one_word.flatMap(lambda line: re.split('[   ,.;:!?]', line['text'])) \
                .map(lambda word: (word, 1)) \
                .reduceByKey(lambda a, b: a + b) \
                .map(lambda e: (e[1], e[0])) \
                .sortByKey(ascending=False)

# Effectue des statistiques sur les dates des tweets
tweet_date = rdd_one_word.map(lambda e: (datetime.datetime.fromtimestamp(int(e['timestamp_ms'])/1000).strftime('%H:%M'), 1)) \
                .reduceByKey(lambda a, b: a+b) \
                .sortByKey()

# Ouverture du fichier pour marquer les réponses
out_path = root_path + '/data/results/' + hashid + '_temp.json'
out = open(out_path, 'w') 
out.write('{')
out.write('"countOneOf":"' + str(rdd_one_word.count()) + '",') # Nombre de tweets contenant au moins un des mots
out.write('"countAll":"' + str(rdd_all_words.count()) + '",') # Nombre de tweets contenant tous les mots

# Les tweets localisés
out.write('"coords":[')
locs = ''
for loc in rdd_coords.collect():
    locs += '[' + str(loc[0]) + ',' + str(loc[1]) + '],'
out.write(locs[:-1] + '],')

# Les 20 mots les plus utilisés
out.write('"mostUsedWords":[')
words = ''
i = 0
for word in word_count.collect():
    the_word = word[1].encode('utf-8')
    if (len(the_word) >= 5 and the_word != 'https'):
        words += '["' + escape_string(the_word) + '",' + str(word[0]) + '],'
        i += 1
        if (i >= 20):
            break
out.write(words[:-1] + '],')

# Nombre de tweets par heure
out.write('"tweetsByTime":[')
dates = ''
for d in tweet_date.collect():
    dates += '["' + d[0] + '",' + str(d[1]) + '],'
out.write(dates[:-1] + ']')

out.write('}')
out.close()

# Déplacement du fichier final
os.rename(out_path, root_path + '/data/results/' + hashid + '.json')
