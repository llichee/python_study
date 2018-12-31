#！/usr/bin/env python
#_*_coding:utf-8 _*_
__author__ = "SmartGo"
age = int(input("plz your age:"))
money = int(input("plz your money:"))
if age >= 18:
	print("你可以进网吧！")
	if money >= 2:
		print("有钱，可以上网！")
	else:
		print("go out!")
else:
	print("未成年人禁止入内")