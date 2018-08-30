#### 一、python实现switch语句
1. 简单示例

![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-6-1/45100834.jpg)

2. 适合一般情形的示例

![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-6-1/81665859.jpg)
***
#### 二、推导式：由已知对象推出另一对象
1. 列表推导式
+ 列表推导式内一般不涉及函数（匿名函数），因为其本身就自带函数的特性
+ map可以是替代方法
+ 下图中的例子用推导式更佳

![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-6-1/98045655.jpg)

2. 元组推导式（一般称为生成器表达式）

![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-6-1/382466.jpg)

3. 集合推导式

![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-6-1/9751812.jpg)

4.字典推导式

![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-6-1/30576515.jpg)

***
#### 三、None与NoneType
+ None是个对象，是NoneType类型
+ None表示空；不等同于空字符串、空列表、空字典。。。

1. if判空的误区

![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-6-1/77360936.jpg)

> 慎用 if a is None

2. 对象与bool值的转换

![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-6-3/931194.jpg)