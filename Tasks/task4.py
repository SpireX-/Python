#! /usr/bin/dev python
# -*- coding:utf8 -*-
import task3

if __name__ == '__main__':
	bytes = [170,255,193]
	for byte in bytes:
		print task3.convert_cc(byte,2),