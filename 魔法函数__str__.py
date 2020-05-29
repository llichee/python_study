class Hero(object):
    def __init__(self, name, atk, hp):
        self.name = name
        self.atk = atk
        self.hp = hp

    #如果定义了魔法函数__str__,就无需定义info函数了
    #__str__用来打印一些信息，return一个字符串，而且只能有self一个参数
    def __str__(self):
        return "英雄名字：%s 攻击力：%d 血量：%d" % (self.name, self.atk, self.hp)

    """
    def info(self):
        print("英雄名字%s" % self.name)
        print("英雄攻击力%d" % self.atk)
        print("英雄血量%d" % self.hp)
    """

gailun = Hero("gailun", 100, 4000)

#如果没有定义__str__，就可以用下面这个打印英雄信息
#gailun.info()

#如果没有定义__str__，下面打印的就是对象的内存地址，如果定义了__str__，则打印的就是__str__里面的return信息
print(gailun)