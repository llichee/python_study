#！/usr/bin/env python
#_*_coding:utf-8 _*_
__author__ = "Xzw"
#字符串的遍历
str = 'hello world'
for i in str:
	print(i, end='')

#列表的遍历
my_list = ['am', 'is', 'are', 'love', 'you']
for list in my_list:
	print(list, end=' ')
#元组的遍历
my_tunple = ('qw','77','ab')
for tunple in my_tunple:
	print(tunple, end=' ')
#字典的遍历
dict = {'apple':'1','orange':'2','lichee':'3','banana':'5'}
#遍历字典的键
for a in dict.keys():
	print("字典键的遍历：%s" % a)
#遍历字典的值
for b in dict.values():
	print("字典值的遍历：%s" % b)
#遍历字典的元组
for c in dict.items():
	print(c)
#分别遍历字典的键和值
for keys,values in dict.items():
	print("keys=%s,values=%s" % (keys,values))

#带下标索引的遍历
char = ['a','b','c']
for i, h in enumerate(char):
	print(i,h)