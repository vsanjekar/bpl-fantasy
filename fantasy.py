__author__ = 'vsanjekar'

# Learn from BPL data
# http://fantasy.premierleague.com/web/api/elements/1/

import requests
import json
from pymongo import MongoClient

# client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.bpl_fantasy
db.players.ensure_index('id', unique=True)

def fetch_player_data():
    more_players = True
    count = 1
    while more_players:
        url = 'http://fantasy.premierleague.com/web/api/elements/' + str(count)
        r = requests.get(url)
        count += 1
        if r.status_code == 404:
            break
        # print r.text
        player_data_json = json.loads(r.text)
        try:
          db.players.insert(player_data_json)
          print "inserted" + str(count)
        except Exception as e:
          print e

def get_player_data():
    cursor = db.players.distinct("team_name")
    for document in cursor:
        print document['team_name']

    cursor = db.players.find()#.sort({"team_name": "-1"})
    # cursor = db.players.find({"first_name": "Juan"})#.sort({"team_name": "-1"})
    for document in cursor:
        # print '{:20s} {:20s}'.format(document['web_name'].decode('utf-8', 'ignore'),
        #                              document['team_name'].decode('utf-8', 'ignore'))
        # print document['team_name']
        print document['first_name'] + " - " + document['first_name']
# fetch_player_data()
get_player_data()
