#！/usr/bin/env python
#_*_coding:utf-8 _*_
class Hero(object):
	"""
	定义一个英雄类，可以移动和攻击
	"""
	#创建对象时，会默认执行构造函数 __init__()
	#如果没有重写构造函数，python或默认创建一个什么都不做的构造函数
	#一个类里面必须有一个构造函数

	#魔法方法：两个下划线开头、两个下划线结尾；
	#在类里面不需要手动调用，而是某些情况下自动执行的方法；
	def __init__(self):
		"""python里的构造函数就是 __init__()"""
		#构造函数： __init__()构造函数是一个特殊的函数，在类实例化的时候会被自动调用；
		#通常用来做初始化或赋值操作
		# 指定生命值
		self.hp = 2600    #实例变量 （对象都可以使用的变量）
		# 指定攻击力
		self.atk = 450
		# 指定护甲值
		self.armor = 200

	def move(self):
		print("正在前往目标地点...")

	def attack(self):
		print("发出一招强力的普通攻击...")

#实例化一个对象 英雄泰达米尔
taidamier = Hero()


#通过对象 获取 实例变量
print("英雄 泰达米尔的生命值：%d" % taidamier.hp)
print("英雄 泰达米尔的攻击力：%d" % taidamier.atk)
print("英雄 泰达米尔的护甲值：%d" % taidamier.armor)




taidamier.move()
taidamier.attack()