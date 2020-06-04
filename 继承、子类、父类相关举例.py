class master(object):
    """定义一个类：该类具有实例变量和实例方法，主要是古法制作煎饼果子"""

    def __init__(self):

        self.kungfu = "古法煎饼果子配方！"  #同名实例变量

    def make_cake(self):  #同名实例方法

        print("[古法]采用 <%s> 制作" % self.kungfu)

class school(object):
    """跟上面的类相似，主要是现代方法制作煎饼果子"""
    def __init__(self):

        self.kungfu = "现代煎饼果子配方！"  #同名实例变量

    def make_cake(self):   #同名实例方法

        print("[现代]采用 <%s> 制作" % self.kungfu)

class pupil(master, school):
    """定义一个子类，继承上面的两个父类，并且自己具有同名的实例变量与实例方法"""

    def __init__(self):

        self.kungfu = "自创煎饼果子配方！"    #同名实例变量

    def make_cake(self):   #同名实例方法

        print("[自创]采用 <%s> 制作" % self.kungfu)

    def make_old_cake(self):      #定义实例方法，引用父类的实例变量和实例方法
        master.__init__(self)     #此处主要为引用父类的实例变量
        master.make_cake(self)    #引用父类的实例方法

    def make_new_cake(self):
        school.__init__(self)
        school.make_cake(self)

damao = pupil()        #根据类pupil创建一个对象
print(damao.kungfu)    #打印对象的实例变量
damao.make_cake()      #引用对象的实例方法

damao.make_old_cake()  #引用父类实例方法
damao.make_new_cake()  #引用父类实例方法