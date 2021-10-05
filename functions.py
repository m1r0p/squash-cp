#!/usr/bin/env python3
 
###### import 

##### local files
from config import (
        OLD_SQUASH_PROJECTS_URL,
        OLD_SQUASH_CASES_URL,
        OLD_SQUASH_USER,
        OLD_SQUASH_PASS,
)

from classes import *

##### libraries
from requests import Request, Session
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


###### functions
#def get_projects():
#    projects = dict()
#    with Session() as s:
#        s.auth = (OLD_SQUASH_USER,OLD_SQUASH_PASS)
#        raw_resp = s.get(OLD_SQUASH_PROJECTS_URL).content.decode()
#    
#    parsed_resp = bs(raw_resp, "lxml")
#    for row in parsed_resp.find_all('tr'):
#        pr_id = row.find('td', attrs={'class':'project-id'})
#        pr_name = row.find('td', attrs={'class':'name'})
#        if pr_id and pr_name != None:
#            projects[pr_id.text] = pr_name.text
#  
#    return projects

def get_projects():
    projects = dict()
    with Session() as s:
        s.auth = (OLD_SQUASH_USER,OLD_SQUASH_PASS)
        raw_resp = s.get(OLD_SQUASH_PROJECTS_URL).content.decode()
    
    parsed_resp = bs(raw_resp, "lxml")
    for row in parsed_resp.find_all('tr'):
        pr_id = row.find('td', attrs={'class':'project-id'})
        pr_name = row.find('td', attrs={'class':'name'})
        if pr_id and pr_name != None:
            projects[pr_id.text] = pr_name.text
  
    return projects




def get_requirements():
    pass

def get_test_cases(id_list):
    pr_dicts = dict()
    #for pr_id in id_list:
    #    pr_dicts[pr_id] = ('pr' + pr_id)
    #    current_pr = pr_dicts.get(pr_id)
    #    globals()[current_pr] = dict()

    #print(type(pr19))
    #for k,v in pr19.items():
    #    print(k,v)

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
        for pr_id in id_list:
            #pr_dicts[pr_id] = ('pr' + pr_id)
            #current_pr = pr_dicts.get(pr_id)
            #globals()[current_pr] = dict()
            ##print(type(current_pr))
            #print(type('pr' + pr_id))


            #print("%s #####################################################################################" % pr_id)
            find_el = driver.find_element_by_id('TestCaseLibrary-' + pr_id)
            #print("id = %s, elem = %s" % (pr_id, find_el.get_attribute('innerHTML')))
            find_el.find_element_by_class_name("jstree-icon").click()
            #find_el = driver.find_element_by_tag_name("ul")
            #find_el = find_el.find_element_by_tag_name("li")
            #find_el = driver.find_element_by_class_name("jstree-closed")
            #find_el = driver.find_element_by_id('TestCaseFolder-535')
            entire_section = driver.find_element_by_id('TestCaseLibrary-' + pr_id).get_attribute('innerHTML')
            parsed_resp = bs(entire_section, "lxml")
            for row in parsed_resp.find_all('li'):
                #res_id = (row.find('li', attrs={'resid'}))
                resid = row.get('resid')
                name = row.get('name')
                #folder_id = row.get('id')
                #current_pr[resid] = name

                print(resid, name)
                #print("####################")

            #for k,v in current_pr.items():
            #    print(k,v)
            #time.sleep(2)

        print(type(pr19))
    

    except Exception as _ex:
        print(_ex)
    finally:
        driver.close()
        driver.quit()


  
    #return test_cases




