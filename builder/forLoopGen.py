#!/usr/bin/python
import sys


#print to screen on the same line
def printf(st):
    sys.stdout.softspace=0
    print (st),

#create a new file
def create():
    print("creating new  file")
    name=raw_input ("enter the name of file:")
    extension=raw_input ("enter extension of file:")
    try:
        name=name+"."+extension
        file=open(name,'w')
        file.write("#include <iostream> \n#include <list>\n#include <string>\n")
        file.write("using namespace std;\nint main()\n{\n")

        file.close()
        return name
    except:
            print("error occured")
            sys.exit(0)

if ( __name__ == "__main__"):
    file=open(create(),'a')


    file.close()
