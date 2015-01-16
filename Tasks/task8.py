#! /usr/bin/dev python
# -*- coding:utf8 -*-
def lowenstein(str1, str2):
	m = len(str1)
	n = len(str2)

	d=[[0 for j in xrange(m+1)] for i in xrange(n+1)]
	for j in xrange(1,n):
		d[0][j] = d[0][j-1]
	for i in xrange(1,m):
		d[i][0] = d[i-1][0]
		for j in xrange(1,n):
			d[i][j] = min(
				d[i-1][j]+1,
				d[i][j-1]+1,
				d[i-1][j-1]+int(str1[i] != str2[j])
				)
	return d

def print_lowenstein(str1, str2):
	print '(',str1,' : ',str2,')'
	ls = lowenstein(str1, str2)
	for i in ls:
		print i

if __name__ == '__main__':
	print print_lowenstein("CONNECT","CONEHEAD")