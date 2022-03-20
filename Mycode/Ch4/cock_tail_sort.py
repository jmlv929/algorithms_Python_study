# 冒泡排序  从小到大排序 鸡尾酒排序 从后往前来
def cock_tail(array = []):
    for i in range((len(array)) // 2):   #遍历数组 n-1 次
        start_index = 0   #起始指示
        end_index = len(array)-1
        #从前向后排序
        flag = True    #指示信号 如果在经历冒泡之后 没有大小交换 就退出循环
        for j in range(start_index,end_index,1):     #从前向后
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                flag = False
        if flag:
            break
        end_index -= 1   #最后一个为最大数  排序完成一个  -1
        #从后向前排序
        for j in range(end_index,start_index,-1):
            if array[j] < array[j-1]:
                temp = array[j]
                array[j] = array[j-1]
                array[j-1] = temp
                flag = False
        if flag:
            break
        start_index += 1  # 排序完成一个最小的在前面， 起始+1 下一次从左向右就不用排序这个数了

if __name__ == "__main__":
    my_list = [3,6,8,9,4,23,9,2,0]
    my_list1 = [4,6,8,3,5,7,3,2,67,8]

    cock_tail(my_list)
    print(my_list)

    cock_tail(my_list1)
    print(my_list1)