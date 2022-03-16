'''

二叉堆的构件  最小堆

二叉堆利用数组实现 主要有 上浮 与 下沉 两种操作
'''

# 上浮操作  将最后一个节点放在合适的位置
def up_heap(array = []):
    # 数组的最后一个元素 上浮
    child_index = len(array) - 1
    #父节点 子节点可能是 坐子节点 或者 右子节点child_index = 2* parent_index + 1(左子节点）  child_index = 2* parent_index + 2(左子节点）
    parent_index = (child_index - 1) // 2  #左子节点是级数  右子节点是偶数 -1之后相反
    temp = array[child_index]
    while child_index > 0 and temp < array[parent_index]:
        array[child_index] = array[parent_index]
        child_index = parent_index
        parent_index = (parent_index - 1) // 2  # 更新父节点
    array[child_index] = temp  # 当子节点的值 不比父节点大了时候 更新

#下沉操作 将给定index的节点下沉到合适位置 这里有index是因为 可以借助这个函数构件二叉堆 将随机完二叉树构建为二叉堆
def down_heap(parent_index = 0, array= []):
    length = len(array)
    temp = array[parent_index]
    child_index = 2 * parent_index + 1  # 左子节点
    while child_index <= length - 1:
        if child_index + 1 <= length - 1:    #存在右子节点
            child_index = child_index if array[child_index] < array[child_index + 1] else child_index + 1  # 选择左右子节点中较小的节点为子节点
        if temp > array[child_index]:
            array[parent_index] = array[child_index]   # 下沉 子节点的值赋值给父节点
            parent_index = child_index
            child_index = child_index *2 + 1
        else:
            break              #节点比任何子节点 都小 则直接跳出循环  构建二叉堆时从index最大构建 所以保证 下面的二叉堆符合规则
    array[parent_index] = temp

def build_heap(array=[]):
    for i in range(len(array) -1, -1, -1):
        down_heap(i, array)


if __name__ == '__main__':
    my_array1 = [1,3,2,6,5,7,8,9,10,0]
    up_heap(my_array1)
    print(my_array1)

    my_array2 = [7, 1 ,3 ,10 ,5 ,2 ,8 ,9 ,6 ]
    build_heap(my_array2)
    print(my_array2)

'''   my_array1
           1
     3         2 
  6    5     7   8
9   10   0


my_array2
           7
      1        3
  10    5   2    8
9   6
'''
