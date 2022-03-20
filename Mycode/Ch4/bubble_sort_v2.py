# 冒泡排序  从小到大排序
def bubble(array = []):
    for i in range(len(array) - 1):   #遍历数组 n-1 次
        flag = True    #指示信号 如果在经历冒泡之后 没有大小交换 就退出循环
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                flag = False
        if flag:
            break

if __name__ == "__main__":
    my_list = [3,6,8,9,4,23,9,2,0]
    my_list1 = [4,6,8,3,5,7,3,2,67,3,8]

    bubble(my_list)
    print(my_list)

    bubble(my_list1)
    print(my_list1)