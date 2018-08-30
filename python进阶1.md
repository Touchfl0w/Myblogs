### JSON
***
#### 一、JSON的定义
1. json是一种轻量级数据交换格式，json是一种数据格式！！
2. json字符串是一种承载形式，表现形式
3. json的对象类型是json众多格式的一种类型，此外还有json数组等。。
4. 所谓json对象特指javascript中对象的一种，在其他语言中无此说法！
4. json格式经过json.loads（反序列化）方法后，转换对应关系：
5. json、javascrpt、typescript均是ECMAscript规范的实现形式，顾json有自己的一套数据类型！并不依附于javascript。

    ![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-5-30/14039783.jpg)

#### 二、实操
+ 各种json概念与loads方法

![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-5-30/94276135.jpg)


+ dumps方法：序列化

![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-5-30/3315471.jpg)

> 可以看出这两个方法实现了json字符串与python数据类型的转换

***
### 二、枚举

1. 枚举的定义与使用方法

+ 获取枚举成员、枚举成员的name以及枚举成员的value的方法

![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-5-30/85681697.jpg))

+ 为什么要用枚举，而不用类、字典等形式？

1. 枚举内的枚举成员不可变！
2. 枚举内枚举成员的name不可重复

![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-5-30/60929686.jpg)

![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-5-30/53180550.jpg)


![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-5-30/78973265.jpg)

2. 枚举的常见操作

![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-5-30/78973265.jpg)

![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-5-30/1669780.jpg)

3. 枚举的使用场景

![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-5-31/51134227.jpg)

![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-5-31/85558180.jpg)

> 根据value取枚举成员：weekdays(1) ->weekdays.MONDAY

> 根据name取枚举成员：weekdays['MONDAY'] -> weekdays.MONDAY

4. 枚举、枚举类型、枚举成员的区别

+ 枚举是一种数据类型，堪比class;枚举==枚举类型，即weekdays
+ 枚举成员是枚举内定义的一系列常量！！即weekdays.MONDAY
+ 枚举成员的name:MONDAY
+ 枚举成员的value:1

5. IntEnum以及unique装饰器

![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-5-31/10724061.jpg)

![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-5-31/59198425.jpg)


