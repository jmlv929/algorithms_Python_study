
'''
求最大公约数

暴力求解！
'''

def get_greatest_common_divisor(a, b):
    big = max(a,b)
    small = min(a,b)
    if small <= 0:
        return ('存在负数！')
    if big % small == 0:
        return small
    else:
        for i in range(small//2,1,-1):
            if small % i == 0 and big % i == 0:
                return i
    return 1

if __name__ == '__main__':
    print(get_greatest_common_divisor(25,5))
    print(get_greatest_common_divisor(100, 75))
    print(get_greatest_common_divisor(99, 55))
    print(get_greatest_common_divisor(7, 2))