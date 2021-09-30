#!/usr/bin/env python3
 
###### import

##### constants

##### functions
from functions import *

###### start 
def main():
    pr_dict = get_projects()
    #for i in pr_dict.keys():
    #    print(i)

    get_test_cases(pr_dict.keys())

if __name__ == "__main__":
    main()

