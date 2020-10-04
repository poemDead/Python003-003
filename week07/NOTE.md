学习笔记

# 面对对象编程
对象：有一类特殊功能（特殊行为）的集合
类的两大成员：属性和方法

# 属性
1. 类属性
    - 在内存内只保存一份
2. 对象属性
    - 每个对象都再内存内保存一份
> human类和亚当夏娃实例的例子

## 查看属性
`Human.__dict___`可以查看属性，另外`dir(Human)`也可以。
第一种结果是字典，第二种结果是list列表，更好操作。

## 添加静态字段
`Human.newattr = 1`就可以添加新的属性
另外`Setattr(list, 'newattr', 'value')`也可以添加属性，但这句代码会报错因为**内置类型不能添加属性和方法**。

## 属性的作用域
- `_age = 0`人为约定不能修改
- `__fly = False`定义后python会自动进行改名，访问会比较复杂，防止被人为修改或者程序修改
- `__dict__`魔术方法的值会随系统发生变化

## 现实object类的所有子类
`print( ().__class__.__bases__[0].__subclasses__() )`
object是所有内置类的父类

# 方法
```python
class Foo(object):
    """类三种方法语法形式"""

    def instance_method(self):
        print("是类的实例方法，只能被实例对象调用")

    @staticmethod
    def static_method():
        print("是静态方法")

    @classmethod
    def class_method(cls):
        print("是类方法")
```
- 普通方法（实例方法）
- 语法糖（@开头的方法）
    - 类方法classmethod，至少有一个cls参数，表示该方法的类
    - 静态方法staticmethod：有类调用，没有参数

## classmethod
类似于Java中的构造函数，但是python中的构造函数有且默认只有一个`_new_`。

## staticmethod
用来做类型的转换或者条件判断后的一些额外处理的逻辑。
通常和类或逻辑不想关，但是单独写出来又有些多余。

# 属性的处理 
`__getattribute__()`和`__getattr__()`可以在类中**对实例获取属性这一行为**进行操作
- 前者对所有属性的访问都会调用该方法，后者适用于未定义的属性
- 同时定义的时候两者的顺序很重要

## `@property`来把方法封装成属性

# 新式类和经典类

# object和type的关系

# 类的继承

# SOLID设计原则
- 单一责任原则The Single Responsibility Principle
    - 比如scrapy的将爬取，下载等规则分成不同的类处理
- 开放封闭原则The Open Closed Principle
    - 扩展开放，修改封闭
    - 如果需要添加新的功能，不要直接去修改代码而是添加新的方法和属性
- 里氏替换原则The Liskov Substitution Principle
    - 子类完全覆盖父类，保证实例化不会混乱
- 依赖倒置原则The Dependency Inversion Principle
- 接口分离原则The Interface Segregation Principle

# 设计模式
- 设计模式用于解决普遍性问题
- 设计模式保证结构的完整性
## 单例模式
1. 对象只存在一个实例
2. `__init__` 和`__new__` 的区别：
    - `__new__`是实例创建之前被调用，返回该实例对象，是静态方法
    - `__init__` 是实例对象创建完成后被调用，是实例方法
    - `__new__` 先被调用，`__init__` 后被调用
    - `__new__` 的返回值（实例）将传递给`__init__` 方法的第一个参数，`__init__` 给这个实例设置相关参数
## 工厂模式
## mixin模式
## 抽象基类
- 抽象基类（abstract base class，ABC）用来确保派生类实现了基类中的特定方法。
- 使用抽象基类的好处：
    - 避免继承错误，使类层次易于理解和维护。
    - 无法实例化基类。
    - 如果忘记在其中一个子类中实现接口方法，要尽早报错。
```python
from abc import ABC
class MyABC(ABC):
pass
MyABC.register(tuple)
assert issubclass(tuple, MyABC)
assert isinstance((), MyABC)
```