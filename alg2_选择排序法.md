#### alg2:选择排序法
１、运行时间
    Ｏ(n*2)
    
    > 单次查找最小/大元素耗时Ｏ（ｎ),排出一个有序列表需要进行ｎ次操作，
    平均耗时Ｏ(n*n)==O(n*2)
    
2、使用场景
    
    可运用于无序列表，但不是最优解
    
３、代码实现

```
def search_min(array):
    """查找列表中的最小数"""
    min_index = 0
    min_num = array[0]
    for i in range(len(array)):
        if array[i] < min_num:
            min_index = i
            min_num = array[i]
    array.pop(min_index)
    return min_num

def selection_sort(array):
    """选择排序"""
    ordered_array = []
    for i in range(len(array)):
        min_num = search_min(array)
        ordered_array.append(min_num)
    return ordered_array

if __name__ == "__main__":
    array = [1, 5, 28, 3, 55, 25, 3, 22, 32]
    ordered_array = selection_sort(array)
    print(ordered_array)
```

![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-8-27/81443019.jpg)

4、　关于数组与链表

![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-8-27/14967928.jpg)

![](http://image-store1.oss-cn-hangzhou.aliyuncs.com/18-8-27/95244218.jpg)

    
    
    