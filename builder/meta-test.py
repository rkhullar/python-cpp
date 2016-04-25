#!/usr/bin/env python

from meta import *

"""
input: program
output: None
creates cpp project
"""
def build(program):
	# massive code
	pass

if __name__ == '__main__':
	p = program()
	p.addvar('a', 'int', 4)
	p.addstmt('assign', 'a', 5)
	p.addstmt('print', 'a')
	print p
	build(p)
