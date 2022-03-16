''''
链表实现二叉树
广度优先遍历  队列实现

'''
from queue import Queue

class Node:
    def __init__(self, data):  #节点属性
        self.data = data
        self.left = None
        self.right = None

def build_tree(input_list = []):   #建立数的结构 前序排列
    if len(input_list) == 0:
        return None
    data = input_list.pop(0)
    if data is None:  #没有对象
        return None
    node = Node(data)
    node.left = build_tree(input_list)         #栈是由层次结构的
    node.right = build_tree(input_list)
    return node #返回是一个 node

def level_order_traversal(node):
    my_queue = Queue()   #创建了一个队列的类 通过导入的类
    my_queue.put(node)
    while not my_queue.empty():
        print(node.data)
        node = my_queue.get()
        if node.left is not None:
            my_queue.put(node.left)
        if node.right is not None:
            my_queue.put(node.right)

if __name__ == "__main__":
    my_list = [3,2,9,None,None,10,None,None,8,None,4,None,None]
    root = build_tree(my_list)     #调用build_tree只返回一个node节点

    print('广度优先遍历：')
    level_order_traversal(root)
    print()


'''
my_list 
                        3  
          2                            8
    9           10             None         4
None  None  None  None                None     None
'''