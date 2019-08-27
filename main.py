# user https://github.com/gsuitedevs/python-samples/blob/master/calendar/quickstart/README.md
# for google api
import json
import datetime
import os.path

import requests
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from cred import *
from TrelloEvent import TrelloEvent

BASE_URL = "https://api.trello.com/1/"
credLine = f"/{board_id}?key={API_key}&token={oauth_token}"

def makeURL(version):
    return BASE_URL + version + credLine

def getJSON(version):
    URL = makeURL(version)
    r = requests.get(URL)
    jr = json.loads(r)
    return jr

def getLabels():
    jr = getJSON('boards')
    return jr['labelName']

def getListsW():
    options = ['Homework','Study']
    def findLabel(item):
        for x in item['labels']:
            if(x['name'] in options):
                return x['name']
        return "N/A"
    jr_lists = getJSON("lists")
    jr_cards = getJSON('cards')
    listHash = {}
    for item_list in jr_lists:
        listName = item_list['name']
        listId = item_list['id']
        listHash[listId] = {'name':listName,'cards':[]}
    for item_card in jr_cards:
        listId = item_card['idList']
        listHash[listId]['cards'].append({'id':item_card['id'],'name':item_card['name'],'type':findLabel(item_card),'due':item_card['due'],'url':item_card['url']})
    return listHash


def getGoogleData(data):
    """"
        This gets all the data from google regarding the data given by the parameters
        @param data a list of partially filled out ClassEvents
    """
    pass

def setGoogleData(data):
    """
        This resets/adds all the dates in google callanders 
        @param data this is a list of Completely filled Class Events
    """
    pass

def main():
    pass

if(__name__=='__main__'):
    # main()
    pass