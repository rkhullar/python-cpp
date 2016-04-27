#!/usr/bin/env python

"""
@author		:	Rajan Khullar
@created	:	04/26/16
@updated	:	04/26/16
"""

ops = {
	'+': lambda x,y: x+y,
	'-': lambda x,y: x-y
}

def op(sym):
	return ops[sym]

def gen(v):
	print type(v).__name__, v

def test(x):
	print x

if __name__ == '__main__':
	f = op('+')
	print f(1, 2)
