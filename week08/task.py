'''
作业一：
区分以下类型哪些是容器序列哪些是扁平序列，哪些是可变序列哪些是不可变序列：
list
tuple
str
dict
collections.deque

答：
容器序列：list,dict,collections.deque,tuple
扁平序列：str

可变序列：list,dict,collections.deque
不可变序列：str, tuple
'''


'''
作业二：
自定义一个 python 函数，实现 map() 函数的功能。
'''
def mymap(func, args):
    r = []
    for i in args:
        r.append(func(i))
    return r

def testfunc(x):
    return x+1

a = mymap(testfunc,[[1,2],[2,3],3,4,5,6,7,8,9])

b = mymap(str,[1,2,3,4,5,6,7,8,9])

'''
作业三：
实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数。
'''
import time
def timer(func):
    def wrapper(*args, **kw):
        start_time = time.time()
        result = func(*args, **kw)
        end_time = time.time()
        print(f"运行了{end_time-start_time}秒")
        return result
    return wrapper

@timer
def test1(x,y):
    time.sleep(1)
    return x+y*x
