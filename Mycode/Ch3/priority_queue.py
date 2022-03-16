
'''

优先队列的实现 利用最大堆 以及最小堆
'''
class Priority_Queue:
    def __init__(self):
        self.array = []
        self.size = 0


    def enqueue(self, element):
        self.size += 1
        self.array.append(element)
        self.up_heap()

    def dequeue(self):
        if self.size == 0:
            raise Exception('优先队列长度为0！')
        head = self.array[0]
        self.array[0] = self.array[self.size-1]
        self.array.pop(0)
        self.size -= 1
        self.up_heap()
        return head

    # 上浮操作  将最后一个节点放在合适的位置
    def up_heap(self):
        # 数组的最后一个元素 上浮
        child_index = len(self.array) - 1
        # 父节点 子节点可能是 坐子节点 或者 右子节点child_index = 2* parent_index + 1(左子节点）  child_index = 2* parent_index + 2(左子节点）
        parent_index = (child_index - 1) // 2  # 左子节点是级数  右子节点是偶数 -1之后相反
        temp = self.array[child_index]
        while child_index > 0 and temp < self.array[parent_index]:
            self.array[child_index] = self.array[parent_index]
            child_index = parent_index
            parent_index = (parent_index - 1) // 2  # 更新父节点
        self.array[child_index] = temp  # 当子节点的值 不比父节点大了时候 更新

    # 下沉操作 将给定index的节点下沉到合适位置 这里有index是因为 可以借助这个函数构件二叉堆 将随机完二叉树构建为二叉堆
    def down_heap(self, parent_index=0):
        length = len(self.array)
        temp = self.array[parent_index]
        child_index = 2 * parent_index + 1  # 左子节点
        while child_index <= length - 1:
            if child_index + 1 <= length - 1:  # 存在右子节点
                child_index = child_index if self.array[child_index] < self.array[
                    child_index + 1] else child_index + 1  # 选择左右子节点中较小的节点为子节点
            if temp > self.array[child_index]:
                self.array[parent_index] = self.array[child_index]  # 下沉 子节点的值赋值给父节点
                parent_index = child_index
                child_index = child_index * 2 + 1
            else:
                break  # 节点比任何子节点 都小 则直接跳出循环  构建二叉堆时从index最大构建 所以保证 下面的二叉堆符合规则
        self.array[parent_index] = temp

if __name__ == "__main__":
    my_queue = Priority_Queue()
    my_queue.enqueue(5)
    print(my_queue.array)

    my_queue.enqueue(6)
    print(my_queue.array)

    my_queue.enqueue(3 )
    print(my_queue.array)

    my_queue.dequeue()
    print(my_queue.array)