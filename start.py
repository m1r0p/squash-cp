#!/usr/bin/env python3
 
###### import

##### constants

##### functions
from functions import *

###### start 
def main():
    resp = get_projects()
    #resp = get_test_cases()

    #print(type(resp))
    for k,v in resp.items():
        print(k,v)
 
if __name__ == "__main__":
    main()

