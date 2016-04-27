#!/usr/bin/env python

"""
@author		:	Rajan Khullar
@created	:	04/02/16
@updated	:	04/27/16
"""

class program:
	def __init__(self):
		self.structs = []
		self.main = []

	def __str__(self):
		o = ''
		for node in self.main:
			o += str(node) + '\n'
		return o

	def addlogic(self, node):
		if node.__class__.__name__ in ['statement', 'variable']:
			self.main.append(node)

	def addvar(self, *args):
		self.main.append(variable(*args))

	def addstmt(self, *args):
		self.main.append(statement(*args))

class struct:
	def __init__(self):
		self.members = []

class variable:
	def __init__(self, name, type, value=None):
		self.name = name
		self.type = type
		self.value = value

	def __str__(self):
		n = str(self.name)
		t = str(self.type)
		v = str(self.value)
		if self.value:
			return '%s %s = %s;' % (t, n, v)
		else:
			return '%s %s;' % (t, n, v)

class list(variable):
	pass

class object(variable):
	pass

class statement:
	def __init__(self, oper, *args):
		self.oper = oper
		self.args = args

	def __str__(self):
		if self.oper == 'assign':
			var = self.args[0]
			exp = self.args[1]
			return '%s = %s;' % (str(var), str(exp))
		if self.oper == 'print':
			o = 'cout'
			for exp in self.args[0]:
				o += ' << ' + str(exp)
			return o + ' << endl;'

if __name__ == '__main__':
	p = program()
	p.addvar('a', 'int', 4)
	p.addstmt('assign', 'a', 5)
	p.addstmt('print', 'a')
	print p
	print p.__class__
