import random

"""精髓：在类里面通过self来调用实例变量和实例方法，在类外部通过对象来调用实例变量和实例方法"""

class Hero(object):
    """英雄类，具有实例变量以及实例方法"""

    def __init__(self, name, skill, hp, atk, armor):

        self.name = name      #英雄名
        self.skill = skill    #英雄技能
        self.hp = hp          #英雄血量
        self.atk = atk        #英雄攻击力
        self.armor = armor    #英雄护甲值

    def __str__(self):
        """魔法方法__str__用来打印一些信息，return一个字符串，而且只能有一个self参数"""
        return "英雄 <%s> 的血量值是 %d,攻击力是 %d, 护甲值是 %d" % (self.name, self.hp, self.atk, self.armor)

    def move(self):
        print("正在赶往solo地点...")

    def attack(self, enemy):
        random_num = random.randint(1, 2)  #注意此处random模块的使用
        reduce_hp = self.atk * random_num - enemy.armor    #此处是计算受伤害的英雄血量减少的值
        if random_num == 2:
            print("产生暴击！")
        print("英雄 <%s> 对 <%s> 释放了技能 <%s> 产生%d的伤害" % (self.name, enemy.name, self.skill, reduce_hp))
        enemy.hp = enemy.hp - reduce_hp    #此处是计算敌人剩余血量


taidamier = Hero('taidamier', "旋风斩", 2000, 400, 200)
gailun = Hero('gailun', "大宝剑", 4000, 200, 400)

round_num = 1
while True:
    input()
    print("\t\t\t当前是 %d 回合" % round_num)
    print(taidamier)
    print(gailun)

    taidamier.move()
    taidamier.attack(gailun)
    if gailun.hp <= 0:
        print("Game Over! %s 体力不支，被 %s 一刀砍倒在地..." % (gailun.name, taidamier.name))
        break
    gailun.move()
    gailun.attack(taidamier)
    if taidamier.hp <= 0:
        print("Game Over! %s 弱不禁风，被 %s 大宝剑劈昏过去..." % (taidamier.name, gailun.name))
        break
    round_num += 1
    print("------" * 20)