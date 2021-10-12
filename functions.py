#!/usr/bin/env python3
 
###### import 

##### local files
from config import (
        OLD_SQUASH_PROJECTS_URL,
        OLD_SQUASH_CASES_URL,
        OLD_SQUASH_USER,
        OLD_SQUASH_PASS,
        NEW_SQUASH_PROJECTS_URL,
        NEW_SQUASH_USER,
        NEW_SQUASH_PASS,

)

from classes import *

##### libraries
import requests
#from requests import Request, Session
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


###### functions

#def get_projects():
#    project_list = list()
#    with Session() as s:
#        s.auth = (OLD_SQUASH_USER,OLD_SQUASH_PASS)
#        raw_resp = s.get(OLD_SQUASH_PROJECTS_URL).content.decode()
#    
#    parsed_resp = bs(raw_resp, "lxml")
#    for row in parsed_resp.find_all('tr'):
#        pr_id = row.find('td', attrs={'class':'project-id'})
#        pr_name = row.find('td', attrs={'class':'name'})
#        if pr_id and pr_name != None:
#            globals()['%s' % pr_id.text] = SquashElement(int(pr_id.text), pr_name.text, 'project', None, 0)
#            project_list.append(globals()['%s' % pr_id.text])
#  
#    return project_list

def get_projects():
    project_list = list()
    raw_resp = requests.get(OLD_SQUASH_PROJECTS_URL, auth=HTTPBasicAuth(OLD_SQUASH_USER,OLD_SQUASH_PASS)).content.decode()
    parsed_resp = bs(raw_resp, "lxml")
    for row in parsed_resp.find_all('tr'):
        pr_id = row.find('td', attrs={'class':'project-id'})
        pr_name = row.find('td', attrs={'class':'name'})
        if pr_id and pr_name != None:
            globals()['%s' % pr_id.text] = SquashElement(int(pr_id.text), pr_name.text, 'project', None, 0)
            project_list.append(globals()['%s' % pr_id.text])
  
    return project_list




def get_requirements():
    pass

def get_test_cases(upper_object_list):
    object_list = list()
    
    driver = webdriver.Firefox(
        executable_path = "./geckodriver"
    )
    
    driver.maximize_window()
    
    try:
        driver.get(url = OLD_SQUASH_CASES_URL)
        driver.find_element_by_id("j_username").send_keys(OLD_SQUASH_USER)
        driver.find_element_by_id("j_password").send_keys(OLD_SQUASH_PASS)
        driver.find_element_by_id("login-form-button-set").click()
        time.sleep(3)
        for upper_object in upper_object_list:
            #tmp_obj_list = list()
            find_el = driver.find_element_by_id('TestCaseLibrary-' + str(upper_object.self_id))
            find_el.find_element_by_class_name("jstree-icon").click()
            entire_section = driver.find_element_by_id('TestCaseLibrary-' + str(upper_object.self_id)).get_attribute('innerHTML')
            parsed_resp = bs(entire_section, "lxml")
            for row in parsed_resp.find_all('li'):
                resid = row.get('resid')
                if int(resid) != upper_object.self_id:
                    name = row.get('name')
                    kind = row.get('rel')
                    globals()['%s' % resid] = SquashElement(int(resid), name, kind, upper_object.self_id, upper_object.sub_level + 1)
                    #print(globals()['%s' % resid].name, globals()['%s' % resid].self_id, globals()['%s' % resid].kind, globals()['%s' % resid].parrent_id)
                    object_list.append(globals()['%s' % resid])
                    upper_object.add_object(int(resid))

            find_el.find_element_by_class_name("jstree-icon").click()
            
        final_list = list()
        final_list.append(upper_object_list)
        final_list.append(object_list)

    

    except Exception as _ex:
        print(_ex)
    finally:
        driver.close()
        driver.quit()


  
    return final_list



def test_api():
    query = {'Accept':'application/json'}
    resp = requests.get(NEW_SQUASH_PROJECTS_URL, auth=HTTPBasicAuth(NEW_SQUASH_USER,NEW_SQUASH_PASS), params=query)

    return resp


