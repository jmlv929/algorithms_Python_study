
#快速排序 应用递归方法

def quick_sort(array=[]):
    if len(array) < 2:
        return array
    else:
        left = [i for i in array[1:]if i < array[0]]
        right = [i for i in array[1:] if i >= array[0]]
        return quick_sort(left) + [array[0]]+ quick_sort(right)

if __name__ == "__main__":
    my_list = [3,6,8,9,4,23,9,2,0]
    my_list1 = [4,6,8,3,5,7,3,2,67,8]

    quick_sort(my_list)
    print(my_list)
    print("排序结果为：",end=' ')
    print(quick_sort(my_list))

    quick_sort(my_list1)
    print(my_list1)
    print("排序结果为：", end=' ')
    print(quick_sort(my_list1))