'''
利用栈 实现二叉树的前序遍历
深度优先遍历
'''

class Node:
    def __init__(self, data):
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

def pre_order_traversal(node):
    stack = []
    while node is not None or len(stack) > 0:
        while node is not None:  #保证每次都是最左的节点
            print(node.data,end = ' ')
            stack.append(node)    #入栈
            node = node.left
        if len(stack) > 0:
            node = stack.pop()   #出栈
            node = node.right

if __name__ == "__main__":
    my_list = [3, 2, 9, None, None, 10, None, None, 8, None, 4, None, None]
    root = build_tree(my_list)  # 调用build_tree只返回一个node节点

    print('前序遍历：')
    pre_order_traversal(root)
    print()

'''
my_list 
                        3  
          2                            8
    9           10             None         4
None  None  None  None                None     None
'''