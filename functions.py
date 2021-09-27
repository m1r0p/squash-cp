#!/usr/bin/env python3
 
###### import 

##### constants
from config import (
        OLD_SQUASH_PROJECTS_URL,
        OLD_SQUASH_USER,
        OLD_SQUASH_PASS,
)

##### libraries
from requests import Request, Session
#from requests.auth import HTTPBasicAuth
 
def get_projects_list():
    #get_auth = requests.get(OLD_SQUASH_PROJECTS_URL, auth=HTTPBasicAuth(OLD_SQUASH_USER,OLD_SQUASH_PASS))
    with Session() as s:
        s.auth = (OLD_SQUASH_USER,OLD_SQUASH_PASS)
        resp = s.get(OLD_SQUASH_PROJECTS_URL)
    return resp.content.decode()

def parse_response(resp):
    pass



