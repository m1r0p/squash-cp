#!/usr/bin/env python3
 
###### import 

##### local files
from config import (
        OLD_SQUASH_USER,
        OLD_SQUASH_PASS,
        OLD_SQUASH_PROJECTS_URL,
        OLD_SQUASH_REQ_URL,
        OLD_SQUASH_CASES_URL,
        OLD_SQUASH_CAMP_URL,
        NEW_SQUASH_PROJECTS_URL,
        NEW_SQUASH_GET_PR_URL,
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
import json

###### functions

def get_projects_from_old_squash():
    project_list = list()
    raw_resp = requests.get(OLD_SQUASH_PROJECTS_URL, auth=HTTPBasicAuth(OLD_SQUASH_USER,OLD_SQUASH_PASS)).content.decode()
    parsed_resp = bs(raw_resp, "lxml")
    for row in parsed_resp.find_all('tr'):
        pr_id = row.find('td', attrs={'class':'project-id'})
        pr_name = row.find('td', attrs={'class':'name'})
        #pr_label = row.find('td', attrs={'class':'label'})
        if pr_id and pr_name != None:
            globals()['%s' % pr_id.text] = SquashProject(int(pr_id.text), pr_name.text, 'project', 0)
            project_list.append(globals()['%s' % pr_id.text])
  
    return project_list


def get_requirements_from_old_squash(upper_object_list):
    object_list = list()
    
    driver = webdriver.Firefox(
        executable_path = "./geckodriver"
    )
    
    driver.maximize_window()
    driver.get(url = OLD_SQUASH_REQ_URL)
    driver.find_element_by_id("j_username").send_keys(OLD_SQUASH_USER)
    driver.find_element_by_id("j_password").send_keys(OLD_SQUASH_PASS)
    driver.find_element_by_id("login-form-button-set").click()
    time.sleep(3)
    for upper_object in upper_object_list:
        #tmp_obj_list = list()
        find_el = driver.find_element_by_id('RequirementLibrary-' + str(upper_object.self_id))
        find_el.find_element_by_class_name("jstree-icon").click()
        entire_section = driver.find_element_by_id('RequirementLibrary-' + str(upper_object.self_id)).get_attribute('innerHTML')
        parsed_resp = bs(entire_section, "lxml")
        for row in parsed_resp.find_all('li'):
            resid = row.get('resid')
            if int(resid) != upper_object.self_id:
                name = row.get('name')
                kind = row.get('rel')
                if kind == 'folder':
                    globals()['%s' % resid] = SquashFolder(int(resid), name, kind, upper_object.sub_level + 1, upper_object.self_id)
                elif kind == 'file':
                    globals()['%s' % resid] = SquashFile(int(resid), name, kind, upper_object.sub_level + 1, upper_object.self_id)
                else:
                    continue

                object_list.append(globals()['%s' % resid])
                upper_object.add_object(int(resid))

        find_el.find_element_by_class_name("jstree-icon").click()
        
    final_list = list()
    final_list.append(upper_object_list)
    final_list.append(object_list)

    driver.close()
    driver.quit()


  
    return final_list



def get_test_cases_from_old_squash(upper_object_list):
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
                    if kind == 'folder':
                        globals()['%s' % resid] = SquashFolder(int(resid), name, kind, upper_object.sub_level + 1, upper_object.self_id)
                    elif kind == 'file':
                        globals()['%s' % resid] = SquashFile(int(resid), name, kind, upper_object.sub_level + 1, upper_object.self_id)
                    else:
                        continue

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

def get_campaigns_from_old_squash(upper_object_list):
    object_list = list()
    
    driver = webdriver.Firefox(
        executable_path = "./geckodriver"
    )
    
    driver.maximize_window()
    
    driver.get(url = OLD_SQUASH_CAMP_URL)
    driver.find_element_by_id("j_username").send_keys(OLD_SQUASH_USER)
    driver.find_element_by_id("j_password").send_keys(OLD_SQUASH_PASS)
    driver.find_element_by_id("login-form-button-set").click()
    time.sleep(3)
    for upper_object in upper_object_list:
        #tmp_obj_list = list()
        find_el = driver.find_element_by_id('RequirementLibrary-' + str(upper_object.self_id))
        find_el.find_element_by_class_name("jstree-icon").click()
        entire_section = driver.find_element_by_id('RequirementLibrary-' + str(upper_object.self_id)).get_attribute('innerHTML')
        parsed_resp = bs(entire_section, "lxml")
        for row in parsed_resp.find_all('li'):
            resid = row.get('resid')
            if int(resid) != upper_object.self_id:
                name = row.get('name')
                kind = row.get('rel')
                if kind == 'folder':
                    globals()['%s' % resid] = SquashFolder(int(resid), name, kind, upper_object.sub_level + 1, upper_object.self_id)
                elif kind == 'file':
                    globals()['%s' % resid] = SquashFile(int(resid), name, kind, upper_object.sub_level + 1, upper_object.self_id)
                else:
                    continue

                #print(globals()['%s' % resid].name, globals()['%s' % resid].self_id, globals()['%s' % resid].kind, globals()['%s' % resid].parrent_id)
                object_list.append(globals()['%s' % resid])
                upper_object.add_object(int(resid))

        find_el.find_element_by_class_name("jstree-icon").click()
        
    final_list = list()
    final_list.append(upper_object_list)
    final_list.append(object_list)

    driver.close()
    driver.quit()

    return final_list



def get_projects_from_new_squash():
    projects_dict = dict()
    query = {'Accept':'application/json'}
    #resp = requests.get(NEW_SQUASH_PROJECTS_URL, auth=HTTPBasicAuth(NEW_SQUASH_USER,NEW_SQUASH_PASS), params=query)
    resp = requests.get(NEW_SQUASH_GET_PR_URL, auth=HTTPBasicAuth(NEW_SQUASH_USER,NEW_SQUASH_PASS))
    
    for i in resp.json()['_embedded']['projects']:
        projects_dict[i['id']] = i['name']


    return projects_dict

def push_projects_to_new_squash(project_list):
    resp_dict = dict()
    with requests.Session() as s: 
        s.auth = HTTPBasicAuth(NEW_SQUASH_USER,NEW_SQUASH_PASS)   
        for pr in project_list:
            pr_data = {
                    '_type':'project',
                    'name': pr.name,
                    'label': '',
                    'description': ''
                    }

            resp = s.post(NEW_SQUASH_PROJECTS_URL, json = pr_data)
            resp_dict[pr.name] = resp


    return resp_dict
