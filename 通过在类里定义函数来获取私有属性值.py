class Person(object):
    def __init__(self, name, age):

        self.name = name
        self.__age = age # 定义一个私有属性

    def get_age(self):
        return self.__age # 在类里面返回私有属性

    def set_age(self, age):
        if 1 > age or age > 100:
            print("INFO:Error!")
        else:
            self.__age = age

p = Person("xxx", 18)
print(p.name)
print(p.get_age())  #通过对象调用函数返回私有属性

p.set_age(300)

