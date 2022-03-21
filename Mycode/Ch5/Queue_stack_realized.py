'''

用栈实现队列

两个栈 A 和 B

入队 直接压入栈A
出队 如果栈B 有元素直接出栈B元素 如果栈B没有元素 栈A有元素 则栈A全部元素出栈 入栈B  出栈B  如果栈A、B都没有元素 输出队列没有元素！！
'''

class Queue_stack:
    def __init__(self):
        self.stack_A = []
        self.stack_B = []

    def en_queue(self, data):
        self.stack_A.append(data)

    def de_queue(self):
        if len(self.stack_B) != 0:
            pop_element = self.stack_B.pop()
        elif len(self.stack_B) == 0 and len(self.stack_A) != 0:
            self.transfer_A_2_B()
            pop_element = self.stack_B.pop()
        else:
            return None
        return pop_element


    def transfer_A_2_B(self):
        for i in range(len(self.stack_A)):
            element = self.stack_A.pop()
            self.stack_B.append(element)

if __name__ == '__main__':
    my_queue = Queue_stack()
    my_queue.en_queue(3)   # A [3]  B []
    my_queue.en_queue(5)     # A [3,5]  B[]
    my_queue.en_queue(9)    # A [3,5,9 ]  B[]
    print(my_queue.stack_A)   # A [3,5,9 ]  B[]

    print(my_queue.de_queue())   # A []  B[9,5]

    my_queue.en_queue(6) # A [6]  B[9,5]

    print(my_queue.stack_A)   # A [6]  B[9,5]
    print(my_queue.stack_B)

    print(my_queue.de_queue())   # A [6]  B[9]
