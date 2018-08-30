#### #practice29:派生内置不可变类型并修改其实例化行为（以tuple为例）

![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-7-28/35855542.jpg)

>  \_\_new\_\_() is intended mainly to allow subclasses of immutable types (like int, str, or tuple) to customize instance creation.

> \_\_init\_\_()Called after the instance has been created (by \_\_new\_\_()), but before it is returned to the caller. 

>  \_\_new\_\_() and \_\_init\_\_() work together in constructing objects (\_\_new\_\_() to create it, and \_\_init\_\_() to customize it)

+ 修改内置不可变类型（int/str/tuple)的实例化行为，做法是：继承内置不可变类，并覆盖其__new__方法。
+ 注意：并非所有内置类都可以简单继承，list/dir/str继承后重新覆盖的某些内置方法会不起作用，即新类还会调用覆盖前的内置方法；为保证不会发生这种情况，最好去继承collections.UserDict/collections.UserList/collections.String
+ __new__负责创建对象，包含创建其大部分内置方法、属性等；__init__负责个性化定制（初始化）对象，即将__init__的参数赋值为对象属性！

1、定制化tuple类型

必须重新定义__new__与__init__

```
class IntTuple(tuple):
	#覆盖tuple的内置静态方法，不需要加装饰器
	def __new__(cls,iterable):
		g = (x for x in iterable if isinstance(x,int) and x > 0)
		return super(IntTuple,cls).__new__(cls,g)

	#参数iterable必须要有，这是数据入口，随后该数据会被传递给__new__
	def __init__(self,iterable):
		print(self)
		#可选
		super(IntTuple,self).__init__()

a = IntTuple([1,44,'2',(3,5)])
```
![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-7-28/18138494.jpg)

***
#### #practice30:减小实例内存开销

![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-7-28/27259118.jpg)

+ 类属性__slots__用于申明实例的所有属性。
+ __dict__属性用于保存对象的所有属性，并可以动态添加
+ 在类属性__slots__中排除__dict__属性，即可禁止对象动态添加属性！如：obj.qq = 100,则对象有了新属性qq

1、 定义类属性__slots__对实例属性的影响

```
import sys
class A():
	def __init__(self,id,name):
		self.id = id
		self.name = name

class B():
	__slots__ = ['id','name']
	def __init__(self,id,name):
		self.id = id
		self.name = name
print(dir(A(1,'lisi')))
print(dir(B(2,'lisi')))
print(set(dir(A(2,'lisi'))) - set(dir(B(2,'lisi'))))
print(sys.getsizeof(A(1,'lisi')))
print(sys.getsizeof(A(1,'lisi').__dict__))
```
![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-7-28/28833516.jpg)

> 属性差异为红色标记的两个属性，__weakref__对于内存的消耗可不计

***
#### practice31:让对象支持上下文管理器

+ 实现上下文管理协议主要依赖类的实例方法__enter__与__exit__
+ 句法 ```with obj as obj1: pass``` ,实际执行过程为obj调用__enter__方法，返回的新对象赋值给obj1,之后执行块内代码，最后obj1执行__exit__方法！

1、实例

```

mydict = {}

class A():
	def __init__(self,a,b):
		self.a = a
		self.b = b
	def __enter__(self):
		mydict['a'] = self.a
		mydict['b'] = self.b
	#后三个参数是固定的，异常类型，异常实例、异常traceback对象
	def __exit__(self,exc_type,exc_val,exc_tb):
		mydict.clear()

print(mydict)
with A(3,5) as Q:
	print(mydict)
print(mydict)

```
![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-7-28/77558374.jpg)

2、异常捕获与压制

```


mydict = {}

class A():
	def __init__(self,a,b):
		self.a = a
		self.b = b
	def __enter__(self):
		mydict['a'] = self.a
		mydict['b'] = self.b
	#后三个参数是固定的，异常类型，异常实例、异常traceback对象
	def __exit__(self,exc_type,exc_val,exc_tb):
		#对于with代码块中出现的异常，__exit__能捕获
		print(exc_type,exc_val,exc_tb)
		mydict.clear()
		#返回True能成功压制异常！！！
		return True

print(mydict)
with A(3,5) as Q:
	raise Exception('myerror')
	print(mydict)
print(mydict)
```
![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-7-28/19327353.jpg)

> with代码块产生异常，但任然会执行__exit__方法，清空字典；这是上下文管理器的默认行为方式，即先执行__exit__后再抛出代码块内的异常，确保__exit__方法始终要执行

> 通过return True成功压制异常,即有异常发生也不抛出！

***
#### #practice32:可管理的对象属性

![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-7-28/38028669.jpg)

+ 直接访问对象属性的形式，如：obj.x = '1',这种方式调用简单，但却不够灵活，例如想要检查属性x的值必须为int,此种方法显然不合适；此外存在安全性问题，如上述赋值后x为str,如果后续进行数学运算，会抛出异常，在程序复杂的情况下很难查找！
+ 使用setx/getx方法来访问属性，相当于中间抽象出一层，进行一些逻辑处理，比较灵活，但每次调用起来比较费劲

+ 解决方法：**内置装饰器property**

```
class circle():
	def __init__(self,radius):
		self.radius = radius

	#get方法（取值器）使用装饰器property
	@property
	#函数名即为新的属性名
	def radius(self):
		#设置器、取值器内部均使用self.__原属性名
		return self.__radius

	#set方法（设置器）使用: 新属性名.setter
	@radius.setter
	def radius(self,value):
		if not isinstance(value,(int,float)):
			raise ValueError('wrong type')
		self.__radius = value

c = circle(100)
print(c.radius)
c.radius = '1'

```
![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-7-28/87279324.jpg)
