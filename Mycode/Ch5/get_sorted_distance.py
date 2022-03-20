
'''

有一个无序整形数组 求出 该数组排序后的任意两个相邻元素的最大差值

要求十时间复杂度 以及 空间复杂度 尽可能低
'''

#可以先进行快速排序 然后遍历找出最大差值 但是 时间复杂度 O(nlogn) 空间复杂度 O(n)

#计数排序

def get_sorted_distance(array=[]):
    min_value = min(array)
    max_value = max(array)
    list_num = max_value - min_value + 1
    #计数排序
    my_list = [] #保存计数0 的个数
    sort_list = [0 for i in range(list_num)]
    for num in array:
        sort_list[num-min_value] += 1
    if 0 not in sort_list:
        return 1    # 相邻元素都有值
    for i in sort_list:
        if i == 0:
            num_0 += 1
            my_list.append(num_0)
        else:
            num_0 = 0
    return max(my_list) + 1

if __name__ == '__main__':
    my_array = [2,6,3,4,5,10,9]
    print(get_sorted_distance(my_array))
