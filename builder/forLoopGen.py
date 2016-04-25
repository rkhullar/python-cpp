#!/usr/bin/python

import xml.sax
import sys

class xmlHandler( xml.sax.ContentHandler ):
   def __init__(self):
       self.cout= ""
       self.str = ""
   # Call when an element starts
   def startElement(self, tag, att):
       if tag == "print":
           self.cout = tag
           printf ("cout<<\"")
           file.write("cout<<\"")

       elif tag == "string":
            self.str = tag

   # Call when an elements ends
   def endElement(self, tag):
       if tag == "string":
           printf ("\"")
           file.write("\"")
       elif tag == "print":
           printf (";")
           file.write(";")

   # Call when a character is read
   def characters(self, content):
       if self.str== "string" and content != "\t" and content != "\n":
           printf (content)
           file.write(content)


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

    # create an XMLReader
    parser = xml.sax.make_parser()
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    # override the default ContextHandler
    Handler = xmlHandler()
    parser.setContentHandler( Handler )
    parser.parse("input.xml")
    file.close()
