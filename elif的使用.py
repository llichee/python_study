#！/usr/bin/env python
#_*_coding:utf-8 _*_
__author__ = "SmartGo"
#根据分数给出优良中差的判断
score = int(input("plz your score:"))
if score >= 90:
	print("优秀")
elif score >=80:
	print("良")
elif score >=60:
	print("中")
elif score <60:
	print("再接再厉")
else:
	print("请输入正确的分数")
