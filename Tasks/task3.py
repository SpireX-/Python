#! /usr/bin/dev python
# -*- coding:utf8 -*-

def convert_cc(num,cc):
	if cc == 10: return num
	if cc <2: return 0

	nums = [];
	while num >= cc:
		a = divmod(num,cc)
		num=a[0]; nums.append(a[1])
	nums.append(num)

	result = ''
	while len(nums)!=0:
		a = nums.pop()
		if cc > 10 and a>9:
			result+=chr(a+ord('A')-10)
		else: result+=str(a)
	return str(result)

if __name__ == "__main__":
	num = 754
	for i in xrange(2,17):
		print "'%s' in cc %s: %s" % (num,i,convert_cc(num,i))