为了使用python实现复杂数据结构与算法，需要借助python内置的基础和数据结构，主要是list和dict,明白这两种数据结构各操作的复杂度对于问题求解以及计算复杂度有着至关重要的作用。
#### 一、list
1、内部使用数组实现

2、缺陷：在头部删除、插入元素复杂度为O(n)，这种情况下，推荐使用collections.deque
![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-10-5/19477188.jpg)

#### 二、dict
![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-10-5/75582666.jpg)

#### 三、参考

标准python内置数据结构操作时间复杂度：

https://wiki.python.org/moin/TimeComplexity