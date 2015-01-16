#! /usr/bin/dev python
# -*- coding:utf8 -*-
#def make_gray(rgb): return [int(0.299*rgb[0] + 0.587*rgb[1] + 0.114*rgb[2])]*3

grayscale = lambda rgb: [int(0.299*rgb[0] + 0.587*rgb[1] + 0.114*rgb[2])]*3
if __name__ == '__main__':
	print grayscale((46,113,45));