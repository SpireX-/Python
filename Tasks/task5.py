#! /usr/bin/dev python
# -*- coding:utf8 -*-
def list_move(l,n): 
	roll_left = n<0 
	n = abs(n)
	while n>0:
		if roll_left:
			tmp = l[0]
			for i in xrange(1,len(l)):
				l[i-1]=l[i]
			l[-1]=tmp
		else: l[0:1]=[l.pop(),l[0]]
		n-=1

if __name__ == '__main__':
	a = range(1,6)
	print a,' -> ',
	list_move(a,-2)
	print a