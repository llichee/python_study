#！/usr/bin/env python
#_*_coding:utf-8 _*_
__author__ = "Xzw"
#定义一个函数，计算任意三个数的和
def sum(x,y,z):
	return x+y+z
#定义另一个函数并调用上一个函数，计算三个数的平均值
def average(x,y,z):
	sumNum=sum(x,y,z)
	avg = sumNum/3
	return avg

print(average(6,6,6))

