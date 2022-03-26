'''
有一个无序整形数组 求出 该数组排序后的任意两个相邻元素的最大差值

要求时间复杂度 以及 空间复杂度 尽可能低

利用桶排序 计算   每个桶只需要记录 入桶的最大值 与 最小值

'''

class Bucket:
    def __init__(self):
        self.min = None
        self.max = None    #桶是一个类 具有最大值 最小值两个属性

def get_sorted_distance_bucket(array=[]):
    #对数组进行桶排序
    max_value = max(array)
    min_value = min(array)
    result = 0 #存储最后的结果
    bucket_num = len(array)   #桶的数量与传入数组的个数相同
    bucket_distance = (max_value - min_value) / (bucket_num-1)  #左闭右开区间 最后一个桶是一个数字
    #建立桶
    bucket_list = [Bucket() for i in range(bucket_num)]  #bucket_num个桶
    #遍历原数组 确定每个桶里面的最大值与 最小值
    for num in array:
        for i in range(bucket_num-1): #前 n-1个桶
            if num >= min_value+bucket_distance*i and num < min_value+ bucket_distance*(i+1):#在i这个桶内
                if bucket_list[i].min is None:   #第一次进桶如果min 或者 max值没有 则将这个值给min或者max
                    bucket_list[i].min = num
                elif bucket_list[i].min is not None and num < bucket_list[i].min:
                    bucket_list[i].min = num
                    # 处理最大值
                if bucket_list[i].max is None:  #保证如果数组只有一个元素进桶 则最大值最小值都是这个数 便于之后的比较 左上限可取桶内的最大值
                    bucket_list[i].max = num
                elif bucket_list[i].max is not None and num > bucket_list[i].max:
                    bucket_list[i].max = num
        if num == max_value:
            bucket_list[bucket_num-1].min = num
            bucket_list[bucket_num-1].max = num
    # 遍历所有的桶 找出最大的相邻差
    right_min = 0
    left_max = 0
    for i in range(bucket_num-1):
        if bucket_list[i].max is not None:    #确保left_max 与 right_min都不是None
            left_max = bucket_list[i].max
        if bucket_list[i+1].min is not None:
            right_min = bucket_list[i+1].min
        if right_min != 0 and left_max != 0:
            result = result if (right_min-left_max)<result else (right_min-left_max)
    return result


    '''
    没有考虑 中间有一个桶最大值 最小值都为空的情况 只是比较相邻两个桶 而且left_max right_min也可能是None
    for i in range(bucket_num-1):   #遍历bucket_num-1次
        left_max = bucket_list[i].max
        right_min = bucket_list[i+1].min
        result = result if (right_min - left_max) < result else (right_min - left_max)
    result = result if (bucket_list[bucket_num-1] - bucket_list[bucket_num-2].max) < result else (bucket_list[bucket_num-1] - bucket_list[bucket_num-2].max)
    '''

if __name__ == "__main__":
    my_array = [2,6,3,4,5,10,9]
    print(get_sorted_distance_bucket(my_array))

    my_array1 = [1,5,9,500,250]
    print(get_sorted_distance_bucket(my_array1))



