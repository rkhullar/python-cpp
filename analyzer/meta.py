#!/usr/bin/env python

"""
@author		:	Rajan Khullar
@created	:	04/02/16
@updated	:	04/06/16
"""

import xml.etree.ElementTree as ET

root = ET.Element('program')
main = ET.SubElement(root, 'main')
p = ET.SubElement(main,'print')
a = ET.SubElement(p,'int')
a.text = 'Hello World'

ET.dump(root)

class Program:
	def __init__(self):
		self.clazzlist = []
		self.main = []

class Clazz:
	def __init__(self):
		self.attributes = []
		self.methods = []

LIST = 1
DICT = 2

class Variable:
	def __init__(self, name, type, struct = None):
		self.name = name
		self.type = type
		self.struct = struct

class Function:
	def __init__(self, name, type = None):
		self.name = name
		self.input = []
		self.type = type
		self.body = []

class Statement:
	pass
