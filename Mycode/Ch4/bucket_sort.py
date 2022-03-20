'''
桶排序 O(n)
分为很多个桶 每个桶存放一个区间  再对每个桶（列表） 进行排序
'''

def bucket_sort(array=[]):
    # 第一步 创建桶 并确定每一个桶的区间范围
    # 很多方式  这里 桶的数量 为 元素的数量  每个桶都是左闭右开 的形式 只有最后一个桶是一个数字
    # 区间长度 = （最大值-最小值）/ （桶的数量-1）
    min_value = min(array)
    max_value = max(array)
    bucket_num = len(array)
    interval_length = (max_value-min_value)/(bucket_num-1)
    #bucket_list = [[]*bucket_num]  # 错误！！ bucket_list = [[]]
    #bucket_list = [[]]*bucket_num    # 桶的列表  每个桶是一个列表[[],[],[],...,[]]
    #bucket_list[1].append(3) 这种不对的 bucket_list = [[3],[3],[3],[3],[3],[3],[3],[3]]  原因是浅拷贝，我们以 bucket_list = [[]]*bucket_num 这种方式创建的列表  bucket_list里面的8个列表的内存是指向同一块，不管我们修改哪个列表，其他几个列表也会跟着改变。
    bucket_list =[[] for j in range(bucket_num)]  #这种方式创建的[[],[],[],[],[],[],[],[]] 改变其中一个不影响其他的
    bucket_list[1].append(3)  # bucket=[[],[3],[],[],[],[],[],[]]
    for i in array:
        for j in range(bucket_num-1):  #寻找前n-1个合适的桶
            if i >= min_value+j*interval_length and i <  min_value+(j+1)*interval_length:
                bucket_list[j].append(i)
                bucket_list[j].sort()
        if i == max_value:   #前n-1个桶 寻找完毕  判断最后一个桶
                bucket_list[bucket_num-1].append(i)
    return bucket_list

if __name__ == "__main__":
    my_list = [4.12,6.421,0.0023,3.0,2.123,8.122,4.12,10.09]
    print(bucket_sort(my_list))