
'''
给出一个整数 从该整数中去掉k个数字（可以是不连续的），要求剩下的数字形成的新整数尽可能小，如果选择去掉的数字？

贪心算法 ！！！
局部最优解 -> 全局最优解

把原整数的所有数字从左到右进行比较 如果发现某一位数字大于它右边的数字 那么在删除该数字之后 必然回事该位的值降低

输入：541 270 936
输出：120936


重点  ： 考虑 k作为外循环  还是 遍历数字作为外循环
'''
# 栈记录了历史顺序

def remove_k_digits(str1, k):
    stack = [] #定义一个栈 存储历史数据
    new_length = len(str1) - k    #str1与k给定 new_length是一个固定的值
    for i in range(len(str1)):
        c = str1[i]
        while len(stack)>0 and stack[len(stack)-1]>c and k>0:  #当栈大于0 并且栈顶数字大于当前数字 并且 没有删除k个数字  while 循环！！
            stack.pop()
            k -= 1
        if '0' == c and len(stack) == 0:  #这是还没有给栈顶添加c  如果c是栈顶而且栈为空 这样相当于 0345 前面的0毫无意义
            new_length -= 1
            if new_length <= 0:
                return '0'   #  如果new_length 原本的值为1 或者 0 返回0
            continue
        stack.append(c)  # 当 k<=0时 直接增加字符串中剩下的字符 while 不起作用
    if new_length <= 0:
        return '0'
    return ''.join(stack[:new_length])    # 返回 后 new_length长度的字符串   字符串的.join方法 利用前面的字符串当做拼接符  比如"-".join('dfc') 'd-f-c'

if __name__ == "__main__":
    print(remove_k_digits("123456789", 3))
    print(remove_k_digits("30200", 1))
    print(remove_k_digits("10", 2))
    print(remove_k_digits("541270936", 3))
    print(remove_k_digits("1593212", 4))
    print(remove_k_digits("10000100002", 2))
    print(remove_k_digits("10000100002", 7))




#错误版本
'''
def remove_k_digits(my_str = '', k = 1):
    stack = []  #栈
    stack_index = [] #存储入栈stack的元素在 str中的位置
    new_length = len(my_str) - k
    if new_length < 0:
        return 'k值大于字符串的长度！'
    if new_length == 0:
        return '0'
    k1 = 0
    str_copy = my_str[:]
    while k1 < k:
        for i in range(len(my_str)):
            if len(stack) == 0:
                stack.append(my_str[i])
                stack_index.append(i)
            elif stack[len(stack)-1] > my_str[i]:   #-------错误 算法理解错误  每次my_str[i] 与栈中栈顶元素都相比 如果k>0  而不是每次只比一次-------
                stack.pop()
                str_copy = delete_index_element(stack_index.pop(), str_copy)  #每次stack栈中出栈 同样删除str当初入栈那个元素

                stack.append(my_str[i])
                stack_index.append(i)   #入栈  存放入栈这个元素在str原来数组中的位置

                k1 += 1   # 增加一次 删除操作
            else:
                stack.append(my_str[i])
                stack_index.append(i)

            if k1 == k:          #如果在没有循环完 str中的元素 已经删除掉了 k 个元素 退出循环
                if i+1 < len(my_str):
                    stack += my_str[i+1:]       # 把str数组中剩下的元素也加上
                break   #打破的是for 循环
    #if k1 == 0: --------错误 ！#循环一遍字符串数字越来越大  考虑循环一次k1值加1  进入下一次循环时 k1 就不是0了 万一 有一次字符串全入栈 就不能剔除这个元素了--------
        if len(my_str) == len(str_copy):
            stack.pop()
            str_copy = delete_index_element(stack_index.pop(), str_copy)
            k1 += 1
        if k1 == k:
            break   #打破的是while循环
        my_str = str_copy[:] # ----切片 不能直接相等---
        stack = []
        stack_index = []   # 重新计算
    return ''.join(stack[:])


def delete_index_element(index, str1):       #删除字符串指定位置的元素   --------错误！！ str1是已经删除之前大数的字符串 而index记录的是my_str也就是未删除之前的index--------
    new_str = ""
    for i in range(0, len(str1)):
        if i != int(index):
            new_str = new_str + str1[i]   #------str1 是字符串 所以是值传递 不会影响原来的数值-------
    return new_str


if __name__ == '__main__':

    print(remove_k_digits("123456789", 3))
    print(remove_k_digits("30200", 1))
    print(remove_k_digits("10", 2))
    print(remove_k_digits("541270936", 3))
    print(remove_k_digits("1593212", 4))   错误输出 131
    print(remove_k_digits("10000100002", 2))
    print(remove_k_digits("10000100002", 7))
    
'''
'''
    123456
    200
    0
    120936
    112
    2
    0
'''
