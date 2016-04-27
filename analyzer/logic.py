#!/usr/bin/env python

"""
@author		:	Rajan Khullar
@created	:	04/02/16
@updated	:	04/26/16
"""

import tpg
import pwrap

#	EXPRL	->	(EXPR comma)* EXPR		$ pwrap.test('sucks')
class magic(tpg.Parser):
	__grammar__ = r"""

	separator	spaces	:	'\s+'		;
	token		comma	:	','			;
	token		number	:	'\d+'		$ int
	token		string	:	'\'.+\''	$ str
	token		assign	:	'='			;
	token		cout	:	'print'		;
	token		add		:	'[+-]'		;

	START	->	cout EXPR/x				;
	EXPR/e	->	number/x				$ e = x
			|	string/x				$ e = x[1:-1]
			;
	"""

	def init_lexer(self):
	    lexer = tpg.NamedGroupLexer(True, 0)
	    lexer.def_separator('spaces', r'\s+')
	    lexer.def_token('comma', r',')
	    lexer.def_token('number', r'\d+', int)
	    lexer.def_token('string', r'\'.+\'', str)
	    lexer.def_token('assign', r'=')
	    lexer.def_token('cout', r'print')
	    lexer.def_token('add', r'[+-]')
	    return lexer

	def START(self, ):
	    r""" ``START -> cout EXPR ;`` """
	    START = None
	    cout = self.eat('cout')
	    x = self.EXPR()
	    return START

	def EXPR(self, ):
	    r""" ``EXPR -> number | string ;`` """
	    _p1 = self.lexer.token()
	    try:
	        x = self.eat('number')
	        e = x
	    except tpg.WrongToken:
	        self.lexer.back(_p1)
	        x = self.eat('string')
	        e = x[1:-1]
	    return e


if __name__ == '__main__':
	m = magic()
	print m("print 'a'")
