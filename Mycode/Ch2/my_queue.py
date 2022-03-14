

#循环队列 充分利用数组的空间
class Myqueue():
     def __init__(self,capacity):  #head 头index  last 尾index
         self.list = [None]*capacity
         self.head = 0
         self.last = 0               #属性

     def enqueue(self,data):
         if (self.last + 1) % len(self.list) == self.head:
             raise Exception("队列满了！！")
         self.list[self.last] = data
         self.last = (self.last + 1) % len(self.list)   #这里不能简单地进行 +1 因为是循环队列

     def dequeue(self):
         if self.head == self.last:
             raise Exception("队列为空！")
         dequeue_element = self.list[self.head]
         self.head = (self.head + 1) % len(self.list)   #指向下一个 #这里不能简单地进行 +1 因为是循环队列
         return dequeue_element
     def output(self):
         i = self.head
         while i != self.last:
             print(self.list[i],end=' ')
             i = (i+1) % len(self.list)     #这里不能简单地进行 +1 因为是循环队列

if __name__ == '__main__':
    myqueue = Myqueue(20)

    myqueue.enqueue(1)
    myqueue.output()
    print()

    myqueue.enqueue(3)
    myqueue.output()
    print()

    myqueue.dequeue()
    myqueue.output()
    print()

    '''
    输出
    1 
    1 3 
    3 
    '''


