#! /usr/bin/dev python
# -*- coding:utf8 -*-
def rem_noabc(string,abc):
	not_exists = set()
	for i,c in enumerate(string):
		exists = False
		for a in abc:
			if c == a: 
				exists=True
				break
		if not exists: not_exists.add(c)
	for c in not_exists:
		string = string.replace(c,'')
	return string

if __name__ == '__main__':
	abc=('a','b','c','d','e','t')
	print rem_noabc("abstract",abc)