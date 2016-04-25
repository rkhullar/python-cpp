#!/usr/bin/env python
from meta import *
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
"""
input: program, folder
output: None
creates folder with cpp project
"""
def build(program):
	# massive code
	o = program.main[0]
	print("#include <iostream> \n#include <list>\n#include <string>")
	print("using namespace std;\nint main()\n{")
	if str(o.__class__) == 'meta.variable':
		print "    "+ str(o.type), o.name,"=", str(o.value) + ";"


if __name__ == '__main__':
	"""	file=open(create(),'a')"""
	p = program()
	p.addvar('a', 'int', 4)
	p.addstmt('assign', 'a', 5)
	p.addstmt('print', 'a')
	"""print p"""
	build(p)
	"""file.close()"""
