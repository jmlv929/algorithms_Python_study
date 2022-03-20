
#从小到大排序 构建最大堆 栈顶元素 与
#最大堆
#下沉操作 将给定index的节点下沉到合适位置 这里有index是因为 可以借助这个函数构件二叉堆 将随机完二叉树构建为二叉堆
def down_heap(parent_index = 0, array= []):
    length = len(array)
    temp = array[parent_index]
    child_index = 2 * parent_index + 1  # 左子节点
    while child_index <= length - 1:    #子节点必须存在于这个数组当中
        if child_index + 1 <= length - 1:    #存在右子节点
            child_index = child_index if array[child_index] > array[child_index + 1] else child_index + 1  # 选择左右子节点中较大的节点为子节点
        if temp < array[child_index]:
            array[parent_index] = array[child_index]   # 下沉 子节点的值赋值给父节点
            parent_index = child_index
            child_index = child_index *2 + 1
        else:
            break              #节点比任何子节点 都小 则直接跳出循环  构建二叉堆时从index最大构建 所以保证 下面的二叉堆符合规则
    array[parent_index] = temp

def heap_sort(array=[]):
    # 构建最大堆
    array1 = []
    for i in range(len(array) -1, -1, -1):
        down_heap(i, array)           #对array数组构建最大堆
    length = len(array)  #存储最开始array的长度  因为down_heap函数对传入的整个数组进行排序
    for i in range(length-1):
        temp = array[0]
        array1.append(temp)          #存储最大值  栈顶
        array[0] = array[length-i-1]
        array[length-i-1] = temp         #  栈顶元素 与 剔除排序好元素之后剩下index最大的元素交换
        #  down_heap(0, array)  这里 不能对 已经放置在叶子节点的数 进行 重新构建了  要去除这些
        array.pop()   #对已经找出的最大值 进行剔除 不再进行down_heap操作
        down_heap(0,array)
    array1 += array  # 经过length -1 次循环 已经找出位于栈顶的各个元素 但是有 length个值 对array1只增加了length-1个元素 剩下一个元素在array中！
    array1.reverse()   #列表反向 append之后最大元素在前
    return array1
'''
#测试最大堆的构建
def build_heap(array=[]):
    # 构建最大堆
    for i in range(len(array) -1, -1, -1):
        down_heap(i, array)
'''
if __name__ == "__main__":
    my_list = [3,6,8,9,4,23,9,2,0]
    my_list1 = [4,6,8,3,5,7,3,2,67,8]

    print(heap_sort(my_list))

    print(heap_sort(my_list1))

'''
    build_heap(my_list)
    print(my_list)
'''

