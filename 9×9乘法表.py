#！/usr/bin/env python
#_*_coding:utf-8 _*_
__author__ = "SmartGo"
i = 1
while i <=9:
	j = 1
	while j <= i:
		print("%d×%d=%d" % (j,i,j*i), end=" ")
		j += 1
	print("\n")
	i += 1

