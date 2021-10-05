#!/usr/bin/env python3
 
from classes import * 
 
def main():
    #a = list()
    #b = dict()
    #for i in range (1, 5):
    #    i = str(i)
    #    a.append(i)

    #for i in a:
    #    b[i] = ('pr' + i)
    #

    #for k,v in b.items():
    #    globals()[v] = dict()
    #    print("%s - %s" %(v,type(v)))

    #print("pr1 - %s" % type(pr1))

    a = SquashElement(222,'ddddddddd')
    
    a.add_object(333)
    for i in a.inner_objects: 
        print(i)

    a.kind = 'pr'
    print(a.kind)
 
if __name__ == "__main__":
    main()

