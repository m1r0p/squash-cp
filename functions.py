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
from bs4 import BeautifulSoup
#import selenium


###### functions
def get_projects():
    projects = dict()
    with Session() as s:
        s.auth = (OLD_SQUASH_USER,OLD_SQUASH_PASS)
        raw_resp = s.get(OLD_SQUASH_URL + '/administration/projects').content.decode()
    
    parsed_resp = BeautifulSoup(raw_resp, "lxml")
    for row in parsed_resp.find_all('tr'):
        pr_id = (row.find('td', attrs={'class':'project-id'}))
        pr_name = (row.find('td', attrs={'class':'name'}))
        if pr_id and pr_name != None:
            projects[pr_id.text] = pr_name.text
  
    return projects

def get_requirements():
    pass

def get_test_cases():
    test_cases = dict()
    with Session() as s:
        s.auth = (OLD_SQUASH_USER,OLD_SQUASH_PASS)
        raw_resp = s.get(OLD_SQUASH_URL + '/test-case-workspace').content.decode()
    
    parsed_resp = BeautifulSoup(raw_resp, "lxml")
    #for row in parsed_resp.find_all('tr'):
    #    pr_id = (row.find('td', attrs={'class':'project-id'}))
    #    pr_name = (row.find('td', attrs={'class':'name'}))
    #    if pr_id and pr_name != None:
    #        projects[pr_id.text] = pr_name.text


  
    return parsed_resp




