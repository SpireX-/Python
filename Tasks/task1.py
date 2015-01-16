#! /usr/bin/dev python
# -*- coding:utf8 -*-
def find_max(a,nums):
	for i in nums:
		if i>a: return i
	return 0

if __name__ == "__main__":
	r = xrange(1,40,5)
	print find_max(11,r)