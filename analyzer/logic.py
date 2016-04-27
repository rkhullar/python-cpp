#!/usr/bin/env python

"""
@author		:	Rajan Khullar
@created	:	04/02/16
@updated	:	04/26/16
"""

import tpg
from pwrap import *

#	EXPRL	->	(EXPR comma)* EXPR		$ pwrap.test('sucks')
class magic(tpg.Parser):
	__grammar__ = r"""

	separator	spaces	:	'\s+'			;
	token		comma	:	','				;
	token		number	:	'\d+'			$ int
	token		string	:	'\'.+\''		$ str
	token		assign	:	'='				;
	token		output	:	'print'			$ ops
	token		var		:	'[a-zA-Z_]\w*'	;
	token		add		:	'[+-]'			;

	START/x		->	output/op EXPR/e	$ x = op(e)			$;
	EXPR/x		->	number/n			$ x = gen(n)
				|	string/s			$ x = gen('"'+s[1:-1]+'"')
				;
	"""

	def init_lexer(self):
	    lexer = tpg.NamedGroupLexer(True, 0)
	    lexer.def_separator('spaces', r'\s+')
	    lexer.def_token('comma', r',')
	    lexer.def_token('number', r'\d+', int)
	    lexer.def_token('string', r'\'.+\'', str)
	    lexer.def_token('assign', r'=')
	    lexer.def_token('output', r'print', ops)
	    lexer.def_token('var', r'[a-zA-Z_]\w*')
	    lexer.def_token('add', r'[+-]')
	    return lexer

	def START(self, ):
	    r""" ``START -> output EXPR ;`` """
	    op = self.eat('output')
	    e = self.EXPR()
	    x = op(e)			
	    return x

	def EXPR(self, ):
	    r""" ``EXPR -> number | string ;`` """
	    _p1 = self.lexer.token()
	    try:
	        n = self.eat('number')
	        x = gen(n)
	    except tpg.WrongToken:
	        self.lexer.back(_p1)
	        s = self.eat('string')
	        x = gen('"'+s[1:-1]+'"')
	    return x


if __name__ == '__main__':
	m = magic()
	print m("print 'b'")
