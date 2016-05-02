#!/usr/bin/env python

"""
@author		:	Rajan Khullar
@created	:	04/02/16
@updated	:	04/30/16
"""

class program:
	def __init__(self):
		self.structs = []
		self.main = []

	def __str__(self):
		return '\n'.join(map(str, self.main))

	def addlogic(self, node):
		if node.__class__.__name__ in ['statement', 'variable']:
			self.main.append(node)

	def addvar(self, *args):
		self.main.append(variable(*args))

	def addstmt(self, *args):
		self.main.append(statement(*args))

	def get(self, mode='variable'):
		out = []
		for node in self.main:
			if node.__class__.__name__ == mode:
				out.append(node)
		return out

	def getvar(self, name):
		for v in self.get('variable'):
			if v.name == name:
				return v
		return -1

	def stats(self):
		return {'stmt':len(self.get('statement')), 'var':len(self.get('variable'))}

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
			return '%s %s;' % (t, n)

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
		for f in [int, float, variable.ibool, str]:
			try:
				return f(s)
			except:
				pass

	@staticmethod
	def ityp(s):
		s = variable.istr(s)
		t = type(s).__name__
		if t != 'str':
			return t
		if s[0] == '\"' and s[-1] == '\"':
			return 'string'
		if '.' in s:
			return 'exp'
		return 'var'

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
			var = str(self.args[0])
			if len(self.args) == 2:
				exp = str(self.args[1])
				return '%s = %s;' % (var, exp)
			if len(self.args) == 3:
				key = str(self.args[1])
				exp = str(self.args[2])
				return '%s->set(%s, %s);' % (var, key, exp)

		if self.oper == 'print':
			l = map(str, self.args[0])
			return 'cout << ' + ' << " " << '.join(l) + ' << endl;'

		if self.oper == 'list':
			var = self.args[0]
			typ = self.args[1]
			return 'list<%s> *%s = new list<%s>();' % (typ, var, typ)

		if self.oper == 'append':
			var = str(self.args[0])
			exp = str(self.args[1])
			return '%s->add(%s);' % (var, exp)

		if self.oper == 'delete':
			var = str(self.args[0])
			return 'delete %s;' % var


if __name__ == '__main__':
	p = program()
	p.addvar('a', 'int', 4)
	p.addstmt('assign', 'a', 5)
	p.addstmt('print', 'a', 2)
	p.addstmt('list', 'c', 'int')
	print p
	print p.__class__.__name__
	print variable.ityp('"lol"')
	"""print p.__class__"""
