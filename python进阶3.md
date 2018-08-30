### 函数式编程
***
#### 一、闭包
1. python一切皆对象

![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-5-31/72755532.jpg)

> 一切皆对象意味着，所有类型均可被赋值，传参~；函数可以当做参数传递，也可以被当做返回值返回；在其他一些语言中函数仅是一段代码块。

2. 闭包的定义与用法

![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-5-31/48858634.jpg)

如何验证是闭包？

![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-6-1/30196953.jpg)

3. 闭包的应用场景
实现计步功能

![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-6-1/82534540.jpg)

> 使用闭包的环境变量而不借助全局变量，实现了良好的封装性！！！

***
#### 二、匿名函数/表达式

1. 匿名表达式的定义

![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-6-1/38845020.jpg)

> expression中经常用到三元表达式，可以做判断

> 一般语言中三元表达式： x > y ? x : y

> python中格式： x if x > y else y

注意：lamba表达式经常结合map、reduce、filter等函数使用

#### 三、map函数：映射

![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-6-1/6649069.jpg)

+ 多变量下的map

![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-6-1/23323688.jpg)

#### 四、reduce函数：归约
1. 定义

![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-6-1/44004039.jpg)

> 标注中多了个x...

#### 四、filter函数

![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-6-1/68758096.jpg)

> filter返回的filter对象也需要借助内置函数或者继承来的函数__list__等来取值！！


***
### 五、装饰器

1. 用到的两个思想

+ 对于函数定义的复杂是可以接受的，但不能忍受函数调用的复杂
+ 函数对于修改应该是封闭的，对于扩展应是开放的

2. 装饰器的定义

    装饰器demo

![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-6-1/93208122.jpg)

> 上述装饰器仅是个demo，并不能在多种函数类型的情况下实现复用！因为wrapper中参数限定死了：只有一个位置参数

> 注意：wrapper中参数名字可以不同于被包装函数的参数名字，wrapper参数泛指一个位置形参！！

从上图可知：装饰器的几大优势：
+ 未改变已创建函数的定义
+ 未改变已创建函数的调用方式
+ 为已创建函数添加了新的模块！！

3. 装饰器装饰后返回的函数是个闭包(没什么实际作用，只是为了加深闭包的理解)

![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-6-1/66541886.jpg)

3. 真正具有**实际使用价值**的装饰器(必须能够装饰多种类型的函数)

面对多种类型函数情况下，装饰器要有普适性才有意义：

![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-6-1/58654284.jpg)

> 可以记忆装饰器内参数的形参：可变位置参数+可变关键字参数=泛指所有类型的参数