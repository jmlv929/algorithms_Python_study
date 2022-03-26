'''

给定两个升序数组 找出这两个数组归并之后新的升序数组的中位数

A: 1 3 5 6 7 10
B: 2 4 5 9 11
median : 5

A: 3 5 7 8 9
B: 1 2 6 7 15
median: 6.5

'''

#暴力解法

def find_median(A, B):
    total = A + B
    total.sort()
    length = len(total)
    if length % 2 == 0:
        median = (total[int(length/2)] + total[int(length/2-1)])/2   # 不加int 会出错 length/2是一个float 即使length是一个偶数
    else:
        median = total[length//2]
    return median

if __name__ == "__main__":
    A1 = [1,3,5,6,7,10]
    B1 = [2,4,5,9,11]
    print(find_median(A1, B1))

    A2 = [3,5,7,8,9]
    B2 = [1,2,6,7,15]
    print(find_median(A2, B2))

'''
5/2 = 2.5

10/2 = 5.0
'''