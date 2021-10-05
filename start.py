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

    test_cases = get_test_cases(pr_dict.keys())
    #for i in test_cases.keys():
    #    print(i)

if __name__ == "__main__":
    main()

