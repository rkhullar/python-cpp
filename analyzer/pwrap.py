#!/usr/bin/env python

"""
@author		:	Rajan Khullar
@created	:	04/26/16
@updated	:	04/30/16
"""

from meta import *

def assign(*args):
	return statement('assign', *args)

operations = {
	'+':		lambda x,y:		x+y,
	'-':		lambda x,y:		x-y,
	'=':		assign,
	'print':	lambda exl:		statement('print', exl)
}

def ops(sym):
	return operations[sym]

def gen(v):
	#print type(v).__name__, v
	return v

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
		return '%s.get(%s)' % (a, x)

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
