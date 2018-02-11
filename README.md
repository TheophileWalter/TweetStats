# TweetStats
Web interface with python server that deliver tweet's statistics with spark on HDFS

## Requirements
- Python 2.7.12
- Spark 2.2.1
- Hadoop 2.7
- A Web Browser (Firefox 💖)

## Usage
Run `python back/server.py 2319` and then go to `http://localhost:2319`  
Graphical tests : `http://localhost:2319/graph-test.html`

## To do list

- [X] Application Front End (HTML/JavaScript web page)
  - [X] Search a Tweet with keywords
  - [X] Graphical summary of the search result
    - [X] Number of tweet founds
    - [X] Geographical repartition
	  - [X] WordsCloud
    - [X] Most used words on these Tweets
    - [X] _Some others statistics_
  - [X] Server query (Javascript)
  - [X] HTML JSon explorer
- [X] Application Back End (python server)
  - [X] Serving files
  - [X] Manage HTTP sessions
  - [X] Execute python code with specials URLs
  - [X] Creating a python object that contains informations about HTTP sessions and parameters
- [X] Request engine on Tweet database (Spark/HDFS)
  - [X] Import JSON file (replace current base or append)
  - [X] Perform queries on database
- [ ] Remove secret NASA hacking code from our code

---

```
( •_•)
( •_•)>⌐■-■
(⌐■_■)
```
