#！/usr/bin/env python
#_*_coding:utf-8 _*_
__author__ = "Xzw"
a = "qwertyuiop"
for i in a:
	print("------")

	if i == "y":
		break
	print(i)
else:
	print("for循环中如果没有执行本程序则执行此语句")

print("=========分割线==========")

for i in a:
	print("-----")
	if i == "y":
		continue
	print(i)
else:
	print("for循环中如果没有执行本程序则执行此语句")