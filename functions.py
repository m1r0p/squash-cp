#!/usr/bin/env python3
 
###### import 

##### constants
from config import (
        OLD_SQUASH_PROJECTS_URL,
        OLD_SQUASH_CASES_URL,
        OLD_SQUASH_USER,
        OLD_SQUASH_PASS,
)

##### libraries
from requests import Request, Session
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


###### functions
def get_projects():
    projects = dict()
    with Session() as s:
        s.auth = (OLD_SQUASH_USER,OLD_SQUASH_PASS)
        raw_resp = s.get(OLD_SQUASH_PROJECTS_URL).content.decode()
    
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
    #test_cases = dict()
    driver = webdriver.Firefox(
            executable_path = "./geckodriver"
    )
    
    driver.maximize_window()
    
    try:
        driver.get(url = OLD_SQUASH_CASES_URL)
        driver.find_element_by_id("j_username").send_keys(OLD_SQUASH_USER)
        driver.find_element_by_id("j_password").send_keys(OLD_SQUASH_PASS)
        driver.find_element_by_id("login-form-button-set").click()
        time.sleep(5)
    except Exception as _ex:
        print(_ex)
    finally:
        driver.close()
        driver.quit()


  
    #return parsed_resp




