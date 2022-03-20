#判断链表是否有环  利用两个指针  快和慢指针  如果有环 则快指针一定会与慢指针有重合
'''
如果求环长：环长 = 每一次速度差 * 前进次数 = 前进次数

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def is_cycle(head):
    fast = head
    slow = head  #快慢指针
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return("链表有环！")
    return("链表无环")



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
    #node7.next = None

    print(is_cycle(node1))

'''

                    1 < -   8     
                    |       ^
                    |       |
5  ->  3  ->  7  ->  2  ->  6
'''