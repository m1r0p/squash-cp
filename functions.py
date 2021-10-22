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
        OLD_SQUASH_REQ_LIB,
        OLD_SQUASH_REQ_FOL,
        OLD_SQUASH_CASES_LIB,
        OLD_SQUASH_CASES_FOL,
        OLD_SQUASH_CAMP_LIB,
        OLD_SQUASH_CAMP_FOL,
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



def find_obj(dr, upper_obj, bso):
    object_list = list()
    find_el = dr.find_element_by_id(bso + str(upper_obj.self_id))
    find_el.find_element_by_class_name("jstree-icon").click()
    #entire_section = find_el.get_attribute('innerHTML')
    parsed_resp = bs(find_el.get_attribute('innerHTML'), "lxml")
    for row in parsed_resp.find_all('li'):
        resid = row.get('resid')
        if int(resid) != upper_obj.self_id:
            name = row.get('name')
            kind = row.get('rel')
            if bso == OLD_SQUASH_REQ_LIB or OLD_SQUASH_REQ_FOL:
                folder_so = OLD_SQUASH_REQ_FOL
            elif bso == OLD_SQUASH_CASES_LIB or OLD_SQUASH_CASES_FOL:
                folder_so = OLD_SQUASH_CASES_FOL
                file_class = CaseFile
            elif bso == OLD_SQUASH_CAMP_LIB or OLD_SQUASH_CAMP_FOL:
                folder_so = OLD_SQUASH_CAMP_FOL
                file_class = CampFile

            if kind == 'file' and (bso == OLD_SQUASH_REQ_LIB or OLD_SQUASH_REQ_FOL):
                #print("#########")
                #print("UPPER - %s" % upper_obj.name)
                #print(name)
                try:
                    find_success = 1
                    find_el.find_element_by_partial_link_text(name).click()
                except:
                    find_success = 0

                if find_success == 1:
                    try:
                        criticality = bs(dr.find_element_by_id('requirement-criticality').get_attribute('innerHTML'), "lxml").text
                    except:
                        criticality = 'Manual selection'
                    try:
                        category = bs(dr.find_element_by_id('requirement-category').get_attribute('innerHTML'), "lxml").text
                    except:
                        category = 'Manual selection'
                    try:
                        status = bs(dr.find_element_by_id('requirement-status').get_attribute('innerHTML'), "lxml").text
                    except:
                        status = 'Manual selection'
                    try:
                        #description = "test"
                        description = bs(dr.find_element_by_id('requirement-description').get_attribute('innerHTML'), "lxml").text
                    except:
                        description = ""



                else:
                    criticality = 'Manual selection'
                    category = 'Manual selection'
                    status = 'Manual'
                    description = ""

                #print(criticality)
                globals()['%s' % resid] = CampFile(
                        int(resid), 
                        name, 
                        kind, 
                        upper_obj.sub_level + 1, 
                        upper_obj.self_id, 
                        criticality, 
                        category,
                        status,
                        description
                        )
                upper_obj.add_object(int(resid))
                object_list.append(globals()['%s' % resid])

            if kind == 'file' and (bso == OLD_SQUASH_CAMP_LIB or OLD_SQUASH_CAMP_FOL):
                #print("#########")
                #print("UPPER - %s" % upper_obj.name)
                #print(name)
                try:
                    find_success = 1
                    find_el.find_element_by_partial_link_text(name).click()
                except:
                    find_success = 0

                if find_success == 1:
                    try:
                        criticality = bs(dr.find_element_by_id('requirement-criticality').get_attribute('innerHTML'), "lxml").text
                    except:
                        criticality = 'Manual selection'
                    try:
                        category = bs(dr.find_element_by_id('requirement-category').get_attribute('innerHTML'), "lxml").text
                    except:
                        category = 'Manual selection'
                    try:
                        status = bs(dr.find_element_by_id('requirement-status').get_attribute('innerHTML'), "lxml").text
                    except:
                        status = 'Manual selection'
                    try:
                        #description = "test"
                        description = bs(dr.find_element_by_id('requirement-description').get_attribute('innerHTML'), "lxml").text
                    except:
                        description = ""



                else:
                    criticality = 'Manual selection'
                    category = 'Manual selection'
                    status = 'Manual'
                    description = ""

                #print(criticality)
                globals()['%s' % resid] = ReqFile(
                        int(resid), 
                        name, 
                        kind, 
                        upper_obj.sub_level + 1, 
                        upper_obj.self_id, 
                        criticality, 
                        category,
                        status,
                        description
                        )
                upper_obj.add_object(int(resid))
                object_list.append(globals()['%s' % resid])



            elif kind == 'folder':
                globals()['%s' % resid] = SquashFolder(int(resid), name, kind, upper_obj.sub_level + 1, upper_obj.self_id)
                upper_obj.add_object(int(resid))
                current_folder = globals()['%s' % resid]
                if 'jstree-closed' in row.get('class'):
                    inner_list = find_obj(dr, current_folder, folder_so)
                    for obj in inner_list:
                        object_list.append(obj)
                    

            else:
                continue

    object_list.append(upper_obj)
    find_el.find_element_by_class_name("jstree-icon").click()

    return object_list


def get_inner_objects_from_old_squash(project_list, base_searching_object):
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
    
    for project in project_list:
        inner_list = find_obj(driver, project, base_searching_object)
        for obj in inner_list:
            object_list.append(obj)
    driver.close()
    driver.quit()
  
    return object_list


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
