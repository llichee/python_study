#！/usr/bin/env python
#_*_coding:utf-8 _*_
__author__ = "Xzw"
#定义一个字典
informain = {'num':'1','name':'xiaozhang','sex':'man','age':27,'address':'Beijing'}
#增加字典内的键值
informain['user'] = 'vip'
#检验是否增加成功
print("增加user后的字典%s" % informain)
print('-' * 50)
#修改字典内的值
informain['num'] = 6
#检验是否修改成功
print('修改后的字典%s' % informain)
print('-'*50)
#查询字典内的元素
print(informain['address'])
print('-' *50)
#删除字典内的元素
del informain['sex']
#查看是否删除成功
print("删除sex后%s" % informain)

#删除整个字典
print("删除前的字典%s" % informain)
del informain
#删除后检验
print('-' *50)
print("删除后的字典%s" % informain)