#!/usr/bin/env python
from meta import *
from phase1 import *


"""
input: program, folder
output: None
creates folder with cpp project
"""
def build(program):
    # massive code
    print("#include <iostream> \n#include <list>\n#include <string>")
    print("using namespace std;\nint main()\n{")

    for x in range(0, len(program.main) ):
        o = program.main[x]
        if str(o.__class__) == 'meta.variable':
            """print '    '+ str(o.type), o.name,"=", str(o.value) + ";"""
        elif str(o.__class__)=="meta.statement":
            if str(o.oper)=="print":
                l = map(str, o.args[0])
                """print ('    '+'cout<<' + '<< " "<<'.join(l) + '<<endl;')"""

        print(o.__class__)

    print ('    return 0;\n'+'}')




if __name__ == '__main__':
    o = phase1('input/parser-2.in')
    o.parse()
    p = o.p
    build(p)
