'''\
最小栈的实现
实现一个栈 具有入栈 出栈 取最小元素的方法 时间复杂度O(n)
设置一个备胎栈B 用于记录历史数据
'''

class Min_stack:
    def __init__(self):
        self.main_stack = []
        self.min_stack = []

    def pop_stack(self):
        if self.min_stack is None:
            return ("栈里已经没有元素！")
        pop_element = self.main_stack.pop()
        if pop_element in self.min_stack:
            self.min_stack.pop()
        return pop_element

    def push_stack(self, data):
        if len(self.main_stack) == 0:
            self.min_stack.append(data)
            self.main_stack.append(data)
        else:
            if data < self.min_stack[len(self.min_stack)-1]:
                self.min_stack.append(data)
            self.main_stack.append(data)

    def get_min(self):
        if len(self.min_stack) == 0:
            return ('栈里没有元素了！！')
        return self.min_stack[len(self.min_stack)-1]

if __name__ == '__main__':
    my_stack = Min_stack()
    my_stack.push_stack(4)
    my_stack.push_stack(5)
    my_stack.push_stack(2)
    my_stack.push_stack(9)
    my_stack.push_stack(1)  # main: [4,5,2,9,1] min: [4,2,1]

    print(my_stack.get_min())

    my_stack.pop_stack()   # main: [4,5,2,9] min: [4,2]
    print(my_stack.get_min())

    my_stack.pop_stack()  # main: [4,5,2] min: [4,2]
    print(my_stack.get_min())

    my_stack.pop_stack()  # main: [4,5] min: [4]
    print(my_stack.get_min())

    my_stack.pop_stack()  # main: [4] min: [4]
    print(my_stack.get_min())

    my_stack.pop_stack()  # main: [] min: []
    print(my_stack.get_min())





