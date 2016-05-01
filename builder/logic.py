#!/usr/bin/env python

"""
@author		:	Rajan Khullar
@created	:	04/02/16
@updated	:	04/30/16
"""

import tpg
from pwrap import *

class magic(tpg.Parser):
	__grammar__ = r"""

	separator	spaces	:	'\s+'					;
	token		natural	:	'\d+'					$ int
	token		string	:	'\'[a-zA-Z0-9_]*\''		$ str
	token		assign	:	'='						$ ops
	token		output	:	'print'					$ ops
	token		var		:	'[a-zA-Z_]\w*'			$ str
	token		add		:	'[+-]'					$ ops

	START/x		->	PRINT/s										$ x = s
				|	ASSIGN/s									$ x = s
				;
	ASSIGN/x	->	var/v assign/op EXPR/e						$ x = op(v,e)
				|	var/v '\[' natural/n '\]' assign/op EXPR/e	$ x = op(v,n,e)
				;
	PRINT/x		->	output/op EXPRL/e							$ x = op(e)	$;
	EXPRL/l		->	EXPR/a										$ l = [a]
				   (
				   	',' EXPR/a									$ l.append(a)
				   )*
				;
	EXPR/x		->	natural/n									$ x = expr('natural', n)
				|	string/s									$ x = expr('string', s)
				|	var/v '\[' natural/n '\]'					$ x = expr('list', v, n)
				|	var/v										$ x = expr('var', v)
				;
	"""

	def init_lexer(self):
	    lexer = tpg.NamedGroupLexer(True, 0)
	    lexer.def_token('_tok_1', r'\[')
	    lexer.def_token('_tok_2', r'\]')
	    lexer.def_token('_tok_3', r',')
	    lexer.def_separator('spaces', r'\s+')
	    lexer.def_token('natural', r'\d+', int)
	    lexer.def_token('string', r'\'[a-zA-Z0-9_]*\'', str)
	    lexer.def_token('assign', r'=', ops)
	    lexer.def_token('output', r'print', ops)
	    lexer.def_token('var', r'[a-zA-Z_]\w*', str)
	    lexer.def_token('add', r'[+-]', ops)
	    return lexer

	def START(self, ):
	    r""" ``START -> PRINT | ASSIGN ;`` """
	    _p1 = self.lexer.token()
	    try:
	        s = self.PRINT()
	        x = s
	    except tpg.WrongToken:
	        self.lexer.back(_p1)
	        s = self.ASSIGN()
	        x = s
	    return x

	def ASSIGN(self, ):
	    r""" ``ASSIGN -> var assign EXPR | var '\[' natural '\]' assign EXPR ;`` """
	    _p1 = self.lexer.token()
	    try:
	        v = self.eat('var')
	        op = self.eat('assign')
	        e = self.EXPR()
	        x = op(v,e)
	    except tpg.WrongToken:
	        self.lexer.back(_p1)
	        v = self.eat('var')
	        self.eat('_tok_1') # '\['
	        n = self.eat('natural')
	        self.eat('_tok_2') # '\]'
	        op = self.eat('assign')
	        e = self.EXPR()
	        x = op(v,n,e)
	    return x

	def PRINT(self, ):
	    r""" ``PRINT -> output EXPRL ;`` """
	    op = self.eat('output')
	    e = self.EXPRL()
	    x = op(e)	
	    return x

	def EXPRL(self, ):
	    r""" ``EXPRL -> EXPR (',' EXPR)* ;`` """
	    a = self.EXPR()
	    l = [a]
	    while True:
	        _p1 = self.lexer.token()
	        try:
	            self.eat('_tok_3') # ','
	            a = self.EXPR()
	            l.append(a)
	        except tpg.WrongToken:
	            self.lexer.back(_p1)
	            break
	    return l

	def EXPR(self, ):
	    r""" ``EXPR -> natural | string | var '\[' natural '\]' | var ;`` """
	    _p1 = self.lexer.token()
	    try:
	        try:
	            n = self.eat('natural')
	            x = expr('natural', n)
	        except tpg.WrongToken:
	            self.lexer.back(_p1)
	            s = self.eat('string')
	            x = expr('string', s)
	    except tpg.WrongToken:
	        self.lexer.back(_p1)
	        try:
	            v = self.eat('var')
	            self.eat('_tok_1') # '\['
	            n = self.eat('natural')
	            self.eat('_tok_2') # '\]'
	            x = expr('list', v, n)
	        except tpg.WrongToken:
	            self.lexer.back(_p1)
	            v = self.eat('var')
	            x = expr('var', v)
	    return x


	""" Alternative / Rejected Regular Expressions:
	EXPRL/l	->	EXPR/a $l=[a]$ (EXPR/a $l.append(a)$)*;
	"""


if __name__ == '__main__':
	m = magic()
	def p(s):
		print s
	t = lambda s: p(m(s))

	# print naturals
	t("print 0")
	t("print 1")
	t("print 99")

	# print strings
	t("print ''")
	t("print 'one'")
	t("print '0N_96b'")

	# print lists
	t("print a")
	t("print b")

	# print lists
	t("print 0, 1, 2, 3")
	t("print 'a', 'b', 'c', 'd'")

	# assignments
	t("a = 5")
	t("b[3] = 'bye'")

	# print list items
	t("print a[2]")
