#!/usr/bin/env python3
 
###### import
##### constants

##### functions
from functions import *

###### start 
def main():
    #pr_list = get_projects_from_old_squash()
    #for i in pr_list:
    #    print(i.self_id)
    #resp = get_projects_from_old_squash()
    #for i in resp:
    #    print(i.name, i.inner_objects)

    #projectest_cases = get_test_cases_from_old_squash(pr_list)
    #or i in test_cases:
    #   for j in i:
    #       if j.kind == 'project':
    #           print("####################################################################################################")
    #           print("id = %s name = %s kind = %s sub_level = %s " % (j.self_id, j.name, j.kind, j.sub_level))
    #           #print("parrent id = %s" % (j.parrent_id))
    #           print("inner objects: %s" % (j.inner_objects))
    resp = get_projects_from_new_squash()
    for k,v in resp.items():
        print("KEY = %s ################# VAL = %s #####################################" % (k, v))
    #print(type(resp))
    #for i in resp:
    #    print("###########UPPER###########################")
    #    print(i)

if __name__ == "__main__":
    main()

