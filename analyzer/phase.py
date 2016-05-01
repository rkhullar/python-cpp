#!/usr/bin/env python

"""
@author		:	Rajan Khullar
@created	:	04/02/16
@updated	:	04/30/16
"""

import tpg, logic, meta

class phaser:
	def __init__(self, filepath):
		self.filepath = filepath
		self.m = logic.magic()
		self.p = meta.program()

	def parse(self):
		with open(self.filepath, 'r') as file:
			for line in file:
				if line.strip():
					try:
						node = self.m(line)
						self.p.addlogic(node)
					except Exception:
						print tpg.exc()
		self.p.sanitize()

if __name__ == '__main__':
	o = phaser('input/parser-1.in')
	o.parse()
	#print o.p.stats()
	print o.p
