

#判断链表是否有环
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def is_cycle(head):
    temp_node = None
    temp_node = head.next
    node_searched = set()   #寻找过的node加入此集合
    node_searched.add(head)
    flag = False
    while temp_node is not None:
        if temp_node in node_searched:
            flag = True
            break
        node_searched.add(temp_node)
        temp_node = temp_node.next
    if flag:
        print("链表有环！")
    else:
        print("链表无环")



if __name__ == '__main__':
    node1 = Node(5)
    node2 = Node(3)
    node3 = Node(7)
    node4 = Node(2)
    node5 = Node(6)
    node6 = Node(8)
    node7 = Node(1)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node4

    is_cycle(node1)

'''

                    1 < -   8     
                    |       ^
                    |       |
5  ->  3  ->  7  ->  2  ->  6
'''





