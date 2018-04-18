def quicksort(array):
    if len(array) < 2:
        return array # 基线条件: 为空或者只包含一个元素的
                     # 数组是有序的
    else:
        pivot = array[0] # 基准值
        # 小于和大于基准值的元素组成子数组
        less  = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)

test_array = [5, 3, 6, 8, 19, 2]
result_array = quicksort(test_array)
print(result_array)
