#!/usr/bin/env python

import ast

if __name__ == '__main__':
	with open('parser-1.in', 'r') as file:
		for line in file:
			if line.strip():
				print ast.parse(line)
