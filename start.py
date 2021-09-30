#!/usr/bin/env python3
 
###### import

##### constants

##### functions
from functions import *

###### start 
def main():
    pr_dict = get_projects()

    get_test_cases(pr_dict.keys())
    #get_test_cases()

    #print(type(resp))
    #for k,v in resp.items():
    #   print(k,v)
    #print(type(pr_dict.keys()))
 
if __name__ == "__main__":
    main()

