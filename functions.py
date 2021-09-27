#!/usr/bin/env python3
 
###### import 

##### constants
from config import (
        OLD_SQUASH_URL,
        OLD_SQUASH_USER,
        OLD_SQUASH_PASS,
)

##### libraries
from requests import Request, Session




###### functions
def get_projects_dict():
    with Session() as s:
        s.auth = (OLD_SQUASH_USER,OLD_SQUASH_PASS)
        resp = s.get(OLD_SQUASH_URL + '/administration/projects').content.decode()
    return resp




