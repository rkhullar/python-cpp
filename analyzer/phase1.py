#!/usr/bin/env python

"""
@author		:	Rajan Khullar
@created	:	04/02/16
@updated	:	04/26/16
"""

import tpg, logic, meta

class phase1:
	def __init__(self, filepath):
		self.filepath = filepath
		self.m = logic.magic()
		self.p = meta.program()

	def parse(self):
		with open(self.filepath, 'r') as file:
			for line in file:
				if line.strip():
					try:
						self.m(line)
					except Exception:
						print tpg.exc()
				else:
					break

if __name__ == '__main__':
	o = phase1('input/parser-1.in')
	o.parse()
	print o.p
