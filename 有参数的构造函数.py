#！/usr/bin/env python
#_*_coding:utf-8 _*_
__author__ = "Xzw"

class Hero(object):

	def __init__(self, name, skill, hp, atk, armor):

		#指定姓名;  self.name是实例变量， name表示实参传递的引用
		self.name = name
		#指定技能
		self.skill = skill
		#指定生命值
		self.hp = hp
		# 指定攻击力
		self.atk = atk
		# 指定护甲值
		self.armor = armor

	def move(self):
		print("正在前往目标地点...")

	def attack(self):
		print("发出一招强力的技能 %s" % self.skill)

	def info(self):
		# 通过对象 获取 实例变量
		print("英雄 %s 的生命值：%d" % (self.name, self.hp))
		print("英雄 %s 的攻击力：%d" % (self.name, self.atk))
		print("英雄 %s 的护甲值：%d" % (self.name, self.armor))

#实例化一个对象 英雄泰达米尔
taidamier = Hero("泰达米尔", "旋风斩", 2600, 460, 200)
taidamier.info()
taidamier.move()
taidamier.attack()

gailun = Hero("盖伦", "大宝剑", 4000, 260, 400)
gailun.info()
gailun.move()
gailun.attack()
