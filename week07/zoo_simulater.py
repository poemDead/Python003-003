'''
背景：在使用 Python 进行《我是动物饲养员》这个游戏的开发过程中，有一个代码片段要求定义动物园、动物、猫、狗四个类。

这个类可以使用如下形式为动物园增加一只猫：

if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = hasattr(z, 'Cat')
具体要求：

定义“动物”、“猫”、“狗”、“动物园”四个类，动物类不允许被实例化。
动物类要求定义“类型”、“体型”、“性格”、“是否属于凶猛动物”四个属性，是否属于凶猛动物的判断标准是：“体型 >= 中等”并且是“食肉类型”同时“性格凶猛”。
猫类要求有“叫声”、“是否适合作为宠物”以及“名字”三个属性，其中“叫声”作为类属性，除凶猛动物外都适合作为宠物，猫类继承自动物类。狗类属性与猫类相同，继承自动物类。
动物园类要求有“名字”属性和“添加动物”的方法，“添加动物”方法要实现同一只动物（同一个动物实例）不能被重复添加的功能。
'''

from abc import ABCMeta, abstractmethod

class Zoo(object):
    def __init__(self,name):
        self.name = name
        self.__animals = []
    
    def add_animal(self,Animal):
        setattr(self,Animal.__class__.__name__,Animal)
        Zoo.no_duplicate_add(self,Animal)
    
    @staticmethod
    def no_duplicate_add(self,Animal):
        if Animal.name not in self.__animals:
            self.__animals.append(Animal.name)
        else:
            print(f'{Animal.name} has already been added.')       


class Animal(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self,catalog,size,personality):
        self.catalog = catalog
        self.size = size
        self.personality = personality
        if ((self.size != '小型') and (self.catalog == '食肉类型') and (self.personality == '性格凶猛')):
            self.ferocious = True
        else:
            self.ferocious = False

class Cat(Animal):
    def __init__(self,name,catalog,size,personality):
        super().__init__(catalog,size,personality)
        self.name = name
        if (self.ferocious == False):
            self.petable = True
        else:
            self.petable = False
            
class Dog(Animal):
    def __init__(self,name,catalog,size,personality):
        super().__init__(catalog,size,personality)
        self.name = name
        if (self.ferocious == False):
            self.petable = True
        else:
            self.petable = False     


if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('Bob','食肉类型','小型','性格温顺')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = hasattr(z, 'Cat')