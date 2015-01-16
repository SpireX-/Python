#! /usr/bin/dev python
# -*- coding:utf8 -*-
import math;

def distance(x1,y1,x2,y2):
	return math.sqrt( pow(x2-x1,2) + pow(y2-y1,2) )

if __name__ == '__main__':
	print distance(0,0,0,10)