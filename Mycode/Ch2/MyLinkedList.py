
#定义一个链表 包括增删 查找功能

class Node:
    def __init__(self, data):  # 一个node节点属性 有 data 以及 next（下一个节点）
        self.data = data
        self.next = None        #是一个Node类的对象

class LinkedList:           #一个链表的属性有 头部节点 尾部节点  链表大小
    def __init__(self):
        self.head = None        #是一个Node类的对象
        self.last = None        #是一个Node类的对象
        self.size = 0

    def get(self, index):
        if index < 0 or index >= self.size:
            raise Exception('查出链表范围！') #Python中的raise 关键字用于引发一个异常
        p = self.head
        for i in range(index):    #链表中根据一个index查找对应的 node
            p = p.next
        return p

    def insert(self, index, data):
        if index < 0 or index > self.size:  # =情况 是可以插入的 这样在插入之后self.zize + 1
            raise Exception("插入超出范围！")
        node = Node(data)
        #空链表的情况
        if self.size == 0:
            self.head = node
            self.last = node
        # 尾部插入
        elif index == self.size:
            self.get(index-1).next = node
            self.last = node
        #头部插入
        elif index == 0:
            node.next = self.head
            self.head = node
        #中间插入
        else:
            node.next = self.get(index)  #查找两次 可继续优化
            self.get(index-1).next = node
        self.size += 1

    def remove(self,index):
        if index < 0 or index >= self.size:   # 情况也不能发生 没有这个节点
            raise Exception("删除超出范围！")
        #尾部删除
        if index == self.size - 1:
            pre_node = self.get(index-1)
            removed_node = pre_node.next
            pre_node.next = None
            self.last = pre_node
        elif index == 0:
            next_node = self.head.next
            removed_node = self.head
            self.head = next_node
        else:
            pre_node = self.get(index - 1)
            removed_node = pre_node.next
            pre_node.next = removed_node.next
        self.size -= 1
        return removed_node

    def output(self):
        p = self.head
        while p is not None:
            print(p.data,end=' ')
            p = p.next


if __name__ == '__main__':
    mylinkedlist = LinkedList()

    mylinkedlist.insert(0,3)
    mylinkedlist.output()
    print ()

    mylinkedlist.insert(0, 1)
    mylinkedlist.output()
    print()

    mylinkedlist.insert(2, 6)
    mylinkedlist.output()
    print()

    mylinkedlist.remove(1)
    mylinkedlist.output()
    print()

    '''
    输出
    3 
    1 3 
    1 3 6 
    1 6 
    '''




