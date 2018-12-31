#！/usr/bin/env python
#_*_coding:utf-8 _*_
__author__ = "SmartGo"
import random
people = int(input("请输入：石头(0)、剪刀(1)、布(2)："))
computer = random.randint(0,2)
if ((people == 0)and(computer == 1)) or ((people == 1)and(computer == 2)) or ((people == 2)and(computer == 0)):
	print("你赢了！")
elif people == computer:
	print("平局")
else:
	print("不要气馁，再来一局")