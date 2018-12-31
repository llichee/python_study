#！/usr/bin/env python
#_*_coding:utf-8 _*_
__author__ = "Xzw"
def name(y):
	sum = 0
	i = 0
	while i <= y:
		sum = sum + i
		i += 1
	return sum

print(name(100))