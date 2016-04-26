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

	def show(self):
		print self.p

	@staticmethod
	def ibool(s):
		s = s.lower()
		if s == 'false':
			return False
		if s == 'true':
			return True
		raise ValueError

	@staticmethod
	def istr(s):
		for f in [int, float, parser.ibool, str]:
			try:
				return f(s)
			except:
				pass

	def parse(self, line):
		a = line.split(' ')
		if len(a) == 1:
			pass
		if len(a) == 2:
			pass
		if len(a) == 3:
			if a[1] == '=':
				var = a[0]
				exp = self.istr(a[2])
				typ = type(exp).__name__
				if var in self.v:
					self.p.addstmt('assign', var, exp)
				else:
					self.p.addvar(var, typ, exp)

if __name__ == '__main__':
	parser('parser-1.in').show()
