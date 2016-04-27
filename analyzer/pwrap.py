#!/usr/bin/env python

"""
@author		:	Rajan Khullar
@created	:	04/26/16
@updated	:	04/26/16
"""

from meta import *

ops = {
	'+': lambda x,y: x+y,
	'-': lambda x,y: x-y
}

def op(sym):
	return ops[sym]

def gen(v):
	#print type(v).__name__, v
	return v

def test(x):
	print x

def out(exp):
	return statement('print', exp)

if __name__ == '__main__':
	f = op('+')
	print f(1, 2)
