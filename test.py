

def search_min(array):
    """查找列表中的最小数"""
    min_index = 0
    min_num = array[min_index]
    for i in range(len(array)):
        if array[i] < min_num:
            min_index = i
            min = array[i]
    return min_num

def selection_sort(array):
    """选择排序"""
    ordered_array = []
    for i in range(len(array)):
        min_num = search_min(array)
        ordered_array.append(min_num)
    return ordered_array

if __name__ = "__main__":
    array = [1, 5, 28, 3, 55, 25,, 3, 22, 32]
    ordered_array = selection_sort(array)
    print(ordered_array)




