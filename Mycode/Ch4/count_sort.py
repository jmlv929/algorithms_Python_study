
#计数排序  对整数进行排序
def count_sort(array=[]):
    count = [0]*11  #数组数值 在0-10之间  一共11个数字
    '''
    这个11 就是 数组中的最大值 + 1
    max_value = array[0]
    for i in range(1,len(array)):
        if array[i] > max_value:
        max_value = array[i]
    count_array = [0] * (max_value + 1) #自动根据数组中最大 确定 级数数组长度 
    '''
    array_sort = [] #存储排过序的数组
    for i in array:
        count[i] = count[i] + 1   #数字与下标关联
    for i in range(len(count)):
        while count[i] >= 1:
            array_sort.append(i)
            count[i] -= 1
    return array_sort

if __name__ == "__main__":
    my_array = [2,4,6,3,6,4,0,9,2,1,8]   #数组 数值 在 0-10之间 整数
    print(count_sort(my_array))