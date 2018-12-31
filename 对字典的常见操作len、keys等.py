#！/usr/bin/env python
#_*_coding:utf-8 _*_
__author__ = "Xzw"
#定义一个字典
dict = {'apple':'1','orange':'2','lichee':'3','banana':'5'}
#查看字典内键值对的个数
print("所有键值对的个数%s" % len(dict))
#查看字典内所有的键
print("字典中所有的键：%s" % dict.keys())
#查看字典中所有的值
print("字典中所有的值：%s" % dict.values())
#返回一个所有包含（键、值）元组的列表
print("字典中所有键值：%s" % dict.items())
