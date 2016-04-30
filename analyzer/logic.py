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
	token		string	:	'\'[a-zA-Z0-9_\s]*\''	$ str
	token		output	:	'print'					$ ops
	token		assign	:	'='						$ ops
	token		append	:	'<<'					$ ops
	token		var		:	'[a-zA-Z_]+'			$ str
	token		type	:	'\$[a-zA-Z_]+'			$ typ
	token		add		:	'[+-]'					$ ops

#	token		type	:	'\$int|\$str'			$ typ

	START/x		->	LIST/s										$ x = s
				|	PRINT/s										$ x = s
				|	ASSIGN/s									$ x = s
				|	APPEND/s									$ x = s
				;
	PRINT/x		->	output/op EXPRL/e							$ x = op(e)		$;

	LIST/x		->	var/v assign type/t '\[\]'					$ x = list(v,t)	$;

	APPEND/x	->	var/v append/op EXPR/e						$ x = op(v,e)	$;

	ASSIGN/x	->	var/v assign/op EXPR/e						$ x = op(v,e)
				|	var/v '\[' natural/n '\]' assign/op EXPR/e	$ x = op(v,n,e)
				;
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
	    lexer.def_token('_tok_1', r'\[\]')
	    lexer.def_token('_tok_2', r'\[')
	    lexer.def_token('_tok_3', r'\]')
	    lexer.def_token('_tok_4', r',')
	    lexer.def_separator('spaces', r'\s+')
	    lexer.def_token('natural', r'\d+', int)
	    lexer.def_token('string', r'\'[a-zA-Z0-9_\s]*\'', str)
	    lexer.def_token('output', r'print', ops)
	    lexer.def_token('assign', r'=', ops)
	    lexer.def_token('append', r'<<', ops)
	    lexer.def_token('var', r'[a-zA-Z_]+', str)
	    lexer.def_token('type', r'\$[a-zA-Z_]+', typ)
	    lexer.def_token('add', r'[+-]', ops)
	    return lexer

	def START(self, ):
	    r""" ``START -> LIST | PRINT | ASSIGN | APPEND ;`` """
	    _p1 = self.lexer.token()
	    try:
	        try:
	            s = self.LIST()
	            x = s
	        except tpg.WrongToken:
	            self.lexer.back(_p1)
	            s = self.PRINT()
	            x = s
	    except tpg.WrongToken:
	        self.lexer.back(_p1)
	        try:
	            s = self.ASSIGN()
	            x = s
	        except tpg.WrongToken:
	            self.lexer.back(_p1)
	            s = self.APPEND()
	            x = s
	    return x

	def PRINT(self, ):
	    r""" ``PRINT -> output EXPRL ;`` """
	    op = self.eat('output')
	    e = self.EXPRL()
	    x = op(e)		
	    return x

	def LIST(self, ):
	    r""" ``LIST -> var assign type '\[\]' ;`` """
	    v = self.eat('var')
	    assign = self.eat('assign')
	    t = self.eat('type')
	    self.eat('_tok_1') # '\[\]'
	    x = list(v,t)	
	    return x

	def APPEND(self, ):
	    r""" ``APPEND -> var append EXPR ;`` """
	    v = self.eat('var')
	    op = self.eat('append')
	    e = self.EXPR()
	    x = op(v,e)	
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
	        self.eat('_tok_2') # '\['
	        n = self.eat('natural')
	        self.eat('_tok_3') # '\]'
	        op = self.eat('assign')
	        e = self.EXPR()
	        x = op(v,n,e)
	    return x

	def EXPRL(self, ):
	    r""" ``EXPRL -> EXPR (',' EXPR)* ;`` """
	    a = self.EXPR()
	    l = [a]
	    while True:
	        _p1 = self.lexer.token()
	        try:
	            self.eat('_tok_4') # ','
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
	            self.eat('_tok_2') # '\['
	            n = self.eat('natural')
	            self.eat('_tok_3') # '\]'
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

	t("print 1")
	t("print 99")

	# print strings
	t("print ''")
	t("print 'one'")
	t("print '0N_96b'")

	# print lists
	t("print a")
	t("print b")

	# print lists	LIST/x		->	var/v '\:' type/t '\[\]'					$ x = list(v,t) $;
	t("print 0, 1, 2, 3")
	t("print 'a', 'b', 'c', 'd'")

	# assignments
	t("a = 5")
	t("b[3] = 'bye'")

	# print list items
	t("print a[2]")

	# create lists
	t("c = $int[]")
	t("d = $box[]")

	## append to lists
	t("s << 'hi'")
