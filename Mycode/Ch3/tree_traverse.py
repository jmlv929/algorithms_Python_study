'''

深度优先遍历
'''
#二叉树的链表实现形式  递归实现  利用递归的回溯特性
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

def pre_order_traversal(node):  #根节点 链表形式 就是根据根节点查找其他节点
    if node is None:
        return                       #啥也不干 也不返回任何东西
    print(node.data,end = ' ')
    pre_order_traversal(node.left)    #调用栈只能访问自己栈内的参数  最底层的栈先排序node左边的
    pre_order_traversal(node.right)
    return node    #返回的是根节点

def in_order_traversal(node):
    if node is None:
        return
    in_order_traversal(node.left)
    print(node.data,end = ' ')                  #调用栈只能访问自己栈内的参数
    in_order_traversal(node.right)
    return node

def post_order_traversal(node):
    if node is None:
        return
    post_order_traversal(node.left)    #调用栈只能访问自己栈内的参数  最底层的栈先排序node左边的
    post_order_traversal(node.right)
    print(node.data, end= ' ')
    return node    #返回的是根节点

if __name__ == "__main__":
    my_list = [3,2,9,None,None,10,None,None,8,None,4,None,None]
    root = build_tree(my_list)     #调用build_tree只返回一个node节点

    print('前序遍历：')
    pre_order_traversal(root)
    print()

    print('中序遍历：')
    in_order_traversal(root)
    print()

    print('后序遍历：')
    post_order_traversal(root)
    print()


'''
my_list 
                        3  
          2                            8
    9           10             None         4
None  None  None  None                None     None
'''





