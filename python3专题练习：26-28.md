#### #practice26:缓存与装饰器（递归子问题）

对于需要重复计算子问题的情况，可以使用缓存，缓存实现有两种方式：1.在函数内定义某种数据结构存储数据 2.使用装饰器（闭包结构）

> 菲波那切数列为：1，1，2，3，5，8，13；即从第三项开始，每一项为前两项之和。

**以菲波那切数列为例**

1、一般的实现方式为：

```
#求第n项的斐波那契数,从0开始
def fibonacci(n):
	if n <= 1:
		return 1
	return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(33))
```
![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-7-7/41019165.jpg)

> 上述函数中由于需要重复计算某些项，所以计算速度非常缓慢，如果在计算过程中能保存一些中间值，速度提升非常明显

![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-7-7/51990549.jpg)

2、使用缓存：保存中间值

```
#方法一：缓存法
#cache以值None层层传递到最底层，然后创建空字典
#cache逐层传递引用，每层的变量cache均指向同一对象！
def fibonacci(n,cache=None):
	if cache is None:
		cache = {}
	if n in cache.keys():
		return cache[n]
	if n <= 1:
		return 1
	cache[n] = fibonacci(n-1,cache) + fibonacci(n-2,cache)
	return cache[n]
	
print(fibonacci(33))
```
> 这种储存中间值的方法不太直观


3、 使用装饰器，利用闭包保存中间值

```
#方法二：使用装饰器，一来不改变函数形式，二可利用闭包保存变量状态，比缓存法容易理解
def decorator(f):
	cache = {}
	def wrapper(*args,**kargs):
		if args not in cache.keys():
			cache[args] = f(*args,**kargs)
		return cache[args]
	return wrapper

@decorator
def fibonacci(n):
	if n <= 1:
		return 1
	return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(33))
```
> 装饰器中闭包的典型使用场景

#### #practice27:函数元数据与装饰器

![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-7-26/26043484.jpg)

1、 函数元数据

```
def f(key,a=1,b=[]):
	'''function f'''
	print(b)
	print(key*2)
#函数名称
print(f.__name__)
#函数注释
print(f.__doc__)
#函数所属模块
print(f.__module__)
#函数的默认参数元组
print(f.__defaults__)
#修改函数参数的默认参数居然成功了，因为元组内包含列表，列表是可变对象！
#正因如此，不应该把可变对象作为参数的默认值！
f.__defaults__[1].append('100')
f(1)
##会报错，元组的元素不可被赋值
#f.__defaults__[0] = 10
#f(1)

def func1():
	a = 3
	return lambda x: a*x
g = func1()
#读取函数的闭包
#每个闭包包含多个cell对象
print(g.__closure__)
#cell对象的cell_contents属性可以读取值
print(g.__closure__[0].cell_contents) 
```

2、 使用装饰器后函数如何保留元数据？

+ 被装饰后的函数，其元数据改为了wrapper函数！

```
def deco(func):
	def wrapper(*args,**kargs):
		'''function wrapper'''
		print("in wrapper")
		func(*args,**kargs)
	return wrapper

def f1(n):
	'''function f1'''
	print(n**2)

print(f1.__name__,f1.__doc__)

@deco
def f2(n):
	'''function f2'''
	print(n**2)
print(f2.__name__,f2.__doc__)
```
![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-7-26/42541029.jpg)

+ 手动修改元数据

```
def deco(func):
	def wrapper(*args,**kargs):
		'''function wrapper'''
		print("in wrapper")
		func(*args,**kargs)
	wrapper.__name__ = func.__name__
	wrapper.__doc__ = func.__doc__
	return wrapper

def f1(n):
	'''function f1'''
	print(n**2)

print(f1.__name__,f1.__doc__)

@deco
def f2(n):
	'''function f2'''
	print(n**2)
print(f2.__name__,f2.__doc__)
```
![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-7-26/36240309.jpg)

+ 使用functools模块中的update_wrapper函数与常量
```
from functools import update_wrapper,WRAPPER_ASSIGNMENTS,WRAPPER_UPDATES

def deco(func):
	def wrapper(*args,**kargs):
		'''function wrapper'''
		print("in wrapper")
		func(*args,**kargs)
	#使用函数update_wrapper更改被装饰后的函数wrapper的元数据
	#参数1：装饰后的函数；参数2：被装饰函数；参数3：指定替换哪些元数据；参数4：指定合并哪些元数据
	update_wrapper(wrapper,func,WRAPPER_ASSIGNMENTS,WRAPPER_UPDATES)
	return wrapper

def f1(n):
	'''function f1'''
	print(n**2)

print(f1.__name__,f1.__doc__)

@deco
def f2(n):
	'''function f2'''
	print(n**2)
print(f2.__name__,f2.__doc__)
#这两个常量皆为元组，一般情况下就使用这两个常量作为update_wrapper的实参
print(WRAPPER_ASSIGNMENTS,WRAPPER_UPDATES)
```
+ 使用functools中的wraps装饰器(带参数)

```
from functools import wraps

def deco(func):
	#带参数装饰器，指定被装饰的函数，替换的元数据任然为WRAPPER_ASSIGNMENTS,WRAPPER_UPDATES
	#效果同上一种方法，不过更简洁
	@wraps(func)
	def wrapper(*args,**kargs):
		'''function wrapper'''
		print("in wrapper")
		func(*args,**kargs)
	return wrapper

def f1(n):
	'''function f1'''
	print(n**2)

print(f1.__name__,f1.__doc__)

@deco
def f2(n):
	'''function f2'''
	print(n**2)
print(f2.__name__,f2.__doc__)
```
> 此为推荐方法

#### #practice28:带参数装饰器

1、示例：实现函数参数类型检查

```
def type(*types,**ktypes):
	def decorator(func):
		def wrapper(*args,**kargs):
			allmatch = True
			for value,_type in zip(args,types):
				if not isinstance(value,_type):
					print("value: " + str(value) + " is not " + str(_type))
					allmatch = False
					break
			if allmatch:
				func(*args,**kargs)
		return wrapper
	return decorator

@type(int,str,int)
def f1(a,b,c):
	print(a,b,c)

@type(int,int,str,tuple)
def f2(a,b,c,d):
	print(a,b,c,d)

f1("s",'qq',55)
f2(1,2,3,4)
f2(1,2,"qq",(22,33))
```

![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-7-27/21815241.jpg)

> 装饰器的参数最终还是要使用在wrapper内！

2、示例：属性可修改的函数装饰器

+ 实现函数运行时间检查

```
import time 
from random import randint
import logging


def runtime(shreshold):
	def decorator(func):
		def wrapper(*args,**kargs):
			start = time.time()
			func(*args,**kargs)
			end = time.time()
			period = end - start
			if period > shreshold:
				msg = '%s:%s > %s' % (func.__name__,period,shreshold)
				logging.warn(msg)
		return wrapper
	return decorator

@runtime(1.5)
def f1():
	print("in test")
	while randint(0,1):
		time.sleep(5)

for _ in range(30):
	f1()
```

+ 使装饰器属性可修改

```
import time 
from random import randint
import logging

def runtime(shreshold):
	def decorator(func):
		def wrapper(*args,**kargs):
			start = time.time()
			func(*args,**kargs)
			end = time.time()
			period = end - start
			if period > shreshold:
				msg = '%s:%s > %s' % (func.__name__,period,shreshold)
				logging.warn(msg)
			def setTimeout(new_shreshold):
				#nonlocal会一直向上查找
				nonlocal shreshold
				shreshold = new_shreshold
			#定义装饰器(本质是函数）的可变属性，该属性为一个函数
			wrapper.setTimeout1 = setTimeout
		return wrapper
	return decorator

@runtime(1.5)
def f1():
	print("in test")
	while randint(0,1):
		time.sleep(1)

if __name__ == "__main__":
	for _ in range(10):
		f1()
	#经过装饰器装饰后的函数f1本质上已经成为wrapper;所以下面是在调用f1的属性罢了
	f1.setTimeout1(2.5)
	for _ in range(10):
		f1()
```
![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-7-27/98879089.jpg)

> 温习一下函数作为一等对象如何定义属性！