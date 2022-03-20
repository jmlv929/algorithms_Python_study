
#计数排序 加强版  稳定排序
def count_sort_stable(array = []):
    min_value = array[0]
    max_value = array[0]
    array_sort = []      #"带有顺序” 的数组
    sorted_array = [None]*len(array)  #长度与array一致  确定顺序的数组
    for i in array:
        if i < min_value:
            min_value = i
        if i > max_value:
            max_value = i
    d = max_value - min_value
    array_cal = [0] * (d+1)  #根据数组中最大值 与 最小值差值确定 计数数组的长度
    #确定array_cal 中的各值的数字
    for i in array:
        array_cal[i-min_value] += 1  # 计数的基础数组求解完毕
    array_sort = array_cal
    for i in range(len(array_cal)-1):
        array_sort[i+1] = array_cal[i] + array_cal[i+1]
    array.reverse()  #从给的数组反序寻找
    for i in array:  #从给的数组反序寻找
        sorted_array[array_sort[i-min_value]-1] = i
        array_sort[i-min_value] -= 1   #下次再遇到相同值 排序-1
    return sorted_array

if __name__ == '__main__':
    my_list = [90,99,95,94,95]
    print(count_sort_stable(my_list))

    my_list1 = [95,94,91,98,99,90,99,93,91,92]
    print(count_sort_stable(my_list1))





