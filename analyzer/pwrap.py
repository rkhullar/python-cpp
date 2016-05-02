#!/usr/bin/env python

"""
@author		:	Rajan Khullar
@created	:	04/26/16
@updated	:	05/01/16
"""

from meta import *

## grammar functions
def assign(*args):
	return statement('assign', *args)

def list(var, type):
	return statement('list', var, type)

def append(*args):
	return statement('append', *args)

## token functions
operations = {
	'+':		lambda x,y:		x+y,
	'-':		lambda x,y:		x-y,
	'print':	lambda exl:		statement('print', exl),
	'=':		assign,
	'<<':		append
}

def ops(sym):
	return operations[sym]

def typ(arg):
	o = str(arg)[1::]
	if o == 'str':
		o = 'string'
	return o

def test(x):
	print type(x).__name__, x
	return x

def expr(mode, a, x=None):
	a = str(a)
	if x:
		x = str(x)
	if mode == 'natural':
		return a
	if mode == 'string':
		return '"'+a[1:-1]+'"'
	if mode == 'var':
		return a
	if mode == 'list':
		return '%s->get(%s)' % (a, x)

if __name__ == '__main__':
	'''
	f = ops('+')
	print f(1, 2)
	f = ops('print')
	print f('a')
	'''
	f = ops('=')
	print f('a', 4, 3)
	print expr('list','a',2)
