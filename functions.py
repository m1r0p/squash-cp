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
    project_list = list()
    with Session() as s:
        s.auth = (OLD_SQUASH_USER,OLD_SQUASH_PASS)
        raw_resp = s.get(OLD_SQUASH_PROJECTS_URL).content.decode()
    
    parsed_resp = bs(raw_resp, "lxml")
    for row in parsed_resp.find_all('tr'):
        pr_id = row.find('td', attrs={'class':'project-id'})
        pr_name = row.find('td', attrs={'class':'name'})
        if pr_id and pr_name != None:
            globals()['%s' % pr_id.text] = SquashElement(int(pr_id.text), pr_name.text, 'project', None)
            project_list.append(globals()['%s' % pr_id.text])
  
    return project_list




def get_requirements():
    pass

def get_test_cases(project_list):
    object_list = list()
    final_list = list()
    
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
        for project in project_list:
            find_el = driver.find_element_by_id('TestCaseLibrary-' + str(project.self_id))
            find_el.find_element_by_class_name("jstree-icon").click()
            entire_section = driver.find_element_by_id('TestCaseLibrary-' + str(project.self_id)).get_attribute('innerHTML')
            parsed_resp = bs(entire_section, "lxml")
            for row in parsed_resp.find_all('li'):
                resid = row.get('resid')
                if int(resid) != project.self_id:
                    name = row.get('name')
                    globals()['%s' % resid] = SquashElement(int(resid), name, 'folder', project.self_id)
                    object_list.append(globals()['%s' % resid])
                    project.add_object(int(resid))
                    #print("current: %s" % project.inner_objects)
            find_el.find_element_by_class_name("jstree-icon").click()
            #print("total: %s" % project.inner_objects)
        final_list.append(project_list)
        final_list.append(object_list)

    

    except Exception as _ex:
        print(_ex)
    finally:
        driver.close()
        driver.quit()


  
    return final_list




