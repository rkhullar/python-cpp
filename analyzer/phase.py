#!/usr/bin/env python

"""
@author		:	Rajan Khullar
@created	:	04/02/16
@updated	:	05/01/16
"""

import tpg, logic
from meta import *

class phaser:
	def __init__(self, filepath):
		self.filepath = filepath
		self.m = logic.magic()
		self.p = program()
		self.vmem = {}	# simple variables
		self.lmem = {}	# list / dict variables

	def parse(self):
		self.parse_syntax()
		self.parse_semantics()
		self.post_clean()

	def parse_syntax(self):
		with open(self.filepath, 'r') as file:
			for line in file:
				if line.strip():
					try:
						node = self.m(line)
						self.p.addlogic(node)
					except Exception:
						print tpg.exc()

	def parse_semantics(self):
		out = []	# new program main
		for node in self.p.get('statement'):
			flag = True
			if node.oper == 'assign':
				o = node.args[0]
				# simple assign
				if len(node.args) == 2:
					if o not in self.vmem:
						flag = False
						exp = node.args[1]
						typ = variable.ityp(exp)
						out.append(variable(o, typ, exp))
						self.vmem[o] = typ
				# list/dict assign
				if len(node.args) == 3:
					if o not in self.lmem:
						key = node.args[1]
						exp = node.args[2]
						typ = variable.ityp(exp)
						out.append(statement('list',o,typ))
						self.lmem[o] = typ
			if flag:
				out.append(node)
		self.p.main = out

	def post_clean(self):
		for o in self.lmem:
			self.p.main.append(statement('delete',o))

if __name__ == '__main__':
	o = phaser('input/parser-1.in')
	o.parse()
	#print o.p.stats()
	print o.p
