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

- [ ] Application Front End (HTML/JavaScript web page)
  - [X] Search a Tweet with keywords
  - [ ] Graphical summary of the search result
    - [ ] Number of tweet founds
    - [X] Geographical repartition
	- [X] WordsCloud
    - [ ] Most used hashtags on these Tweets
    - [ ] _Some others statistics_
  - [X] Server query (Javascript)
  - [X] HTML JSon explorer
- [ ] Application Back End (python server)
  - [X] Serving files
  - [X] Manage HTTP sessions
  - [X] Execute python code with specials URLs
  - [ ] Creating a python object that contains informations about HTTP sessions and parameters
- [ ] Request engine on Tweet database (Spark/HDFS)
  - [ ] Import JSON file (replace current base or append)
  - [ ] Perform queries on database
  - [ ] Delete database
  - [ ] Make a list of most used words in the database for search auto-complete
- [ ] Remove secret NASA hacking code from our code

---

```
( •_•)
( •_•)>⌐■-■
(⌐■_■)
```
