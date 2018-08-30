从今天开始，博主准备开始一段常见算法的学习，算法实现使用Python3,希望坚持下去^_^

#### alg1:二分查找法

1、运行时间
	二分查找相比于依次查找，查询速度提升明显：
	+ 依次查找：O(n)
	+ 二分查找：O（logn)

> n表示候选数的数目；O（logn）实际代表找到目标数需要的查询次数；实际上查询次数可以大概代表运行时间

2、适用场景

排好顺序的列表（python)

3、代码实现

```
from random import randint

def search(list1,target):
	low = 0
	high = len(list1) - 1
	while low < high:
		mid = int((high + low) / 2)
		guess = list1[mid]
		if guess < target: 
		    #+1非常关键，是最终退出循环的决定因素
			low = mid + 1
		elif guess > target:
			high = mid -1
		else:
			return mid
	return None
#生成随机顺序列表
mylist = [i for i in range(1,100) if randint(0,1)]
print(mylist)
print(search(mylist,10))
print(search(mylist,11))
```
![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-7-9/51383806.jpg)

4、几个基础概念

![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-7-9/39614955.jpg)