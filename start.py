#!/usr/bin/env python3
 
###### import
##### constants

##### functions
from functions import *

###### start 
def main():
    pr_list = get_projects_from_old_squash()

    req = get_inner_objects_from_old_squash(pr_list, OLD_SQUASH_REQ_LIB)
    for i in req:
        if i.kind == 'file':
           print("####################################################################################################")
           print("id = %s #### name = %s #### sub_level = %s " % (i.self_id, i.name, i.sub_level))
           print("parrent id = %s" % (i.parrent_id))
           print("criticality: %s" % (i.criticality))
           print("category: %s" % (i.category))
           print("status: %s" % (i.status))
           print("description: %s" % (i.description))

    #get_users_from_old_squash()





if __name__ == "__main__":
    main()

