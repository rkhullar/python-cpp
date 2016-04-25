#!/usr/bin/env python

"""
@author		:	Rajan Khullar
@created	:	04/25/16
@updated	:	04/25/16
"""

from meta import *

class parser:
	def __init__(self, filepath):
		self.p = program()
		self.v = {}
		with open(filepath, 'r') as file:
			for line in file:
				if line.strip():
					self.parse(line.strip())

	def parse(self, line):
		a = line.split(a)
		print a

if __name__ == '__main__':
	parser('parser-1.in')
