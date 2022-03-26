'''

给出一个整数 找出这个正整数所有数字排列的下一个数
输入12345
输出 12354

输入12354
输出 12435

为了和原数接近 尽量保持高位不变 地位在最小范围内变换顺序  变换顺序的范围 取决于逆序范围
'''

def find_nearest_big_number(number=[]):
    # 1. 从后向前查看逆序区域 找到逆序区的前一位 也就是交换的边界
    transfer_point = find_transfer_point(number)
    if transfer_point == 0:
        return ('这个数是最大的了！')
    number_copy = number.copy()  #拷贝一份新的  如果传入number number实际就变了
    exchange_head(transfer_point, number_copy)   #2. 让逆序区的前一位和逆序区中大于它的最小的数字交换位置
    # 3. 把原来的逆序区转变为顺序状态
    reverse(transfer_point, number_copy)
    return number_copy

def exchange_head(index, number = []):
    head = number[index-1]
    for i in range(len(number)-1,0,-1):      #从右开始向左找 找到逆序区比靠近逆序区大的
        if head < number[i]:
            number[index-1] = number[i]
            number[i] = head
            break
    return number

def reverse(index, number=[]):
    left = index
    right = len(number)-1
    while left < right:   #逆序区
        temp = number[left]
        number[left] = number[right]
        number[right] = temp
        left += 1
        right -= 1
    return number

def find_transfer_point(number=[]): #找到逆序区的前一位
    for i in range(len(number)-1, 0, -1):
        if number[i-1] < number[i]:
            return i        #返回逆序区中左边界点
    return 0

if __name__ == "__main__":
    my_list1 = [1,2,3,4,5]
    my_list2 = [1,2,3,5,4]
    print(find_nearest_big_number(my_list1))
    print(find_nearest_big_number(my_list2))