#!/usr/bin/env python

"""
@author		:	Rajan Khullar
@created	:	04/26/16
@updated	:	04/26/16
"""

from meta import *

operations = {
	'+':		lambda x,y: x+y,
	'-':		lambda x,y: x-y,
	'=':		lambda v,e:	statement('assign', v, e),
	'print':	lambda exl: statement('print', exl)
}

def ops(sym):
	return operations[sym]

def gen(v):
	#print type(v).__name__, v
	return v

def test(x):
	print type(x).__name__, x
	return x

if __name__ == '__main__':
	f = ops('+')
	print f(1, 2)
	f = ops('print')
	print f('a')
