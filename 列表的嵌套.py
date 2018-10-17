#！/usr/bin/env python
#_*_coding:utf-8 _*_
__author__ = "Xzw"
#将"ABCDEFGH"八位老师，随机分配到列表my_list中（办公室）
import random
#定义八位老师
teacher = 'ABCDEFGH'
#定义三间办公室
my_list = [[],[],[]]
for name in teacher:
	#随机分配索引0，1，2
	index = random.randint(0,2)
	#根据随机索引，在my_list中增加元素
	my_list[index].append(name)

print(my_list)
i = 1
#遍历my_list元素
for list_my in my_list:
	#格式化输出办公室人数
	print("办公室%d的人数：%d" %(i,len(list_my)))
	i += 1
	#遍历每间办公室的老师
	for list_me in list_my:
		#格式化输出每间办公室老师的名字
		print("%s" % list_me, end='')
	print("\n")
	print('_' * 20)
