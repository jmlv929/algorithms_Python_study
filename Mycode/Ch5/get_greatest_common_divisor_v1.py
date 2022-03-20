'''
v1辗转相处法
基于： 两个正整数a和b (a>b)，它们的最大公约数等于 a除以 b的余数c 和b之间的最大公约数

v2 更相减损术
两个正整数a和b（a>b） 它们的最大公约数等于a-b的差值c和较小数b的最大公约数  递归 直到两个数相等
'''

def get_greatest_common_divisor_v1(a, b):
    big = max(a, b)
    small = min(a, b)
    if small <= 0:
        return ('存在负数！')
    if small == 1:
        return 1
    if big % small == 0:
        return small
    else:
        return get_greatest_common_divisor_v1(big%small, small)

def get_greatest_common_divisor_v2(a, b):
    big = max(a, b)
    small = min(a, b)
    if small <= 0:
        return ('存在负数！')
    if small == 1:
        return 1
    if big == small :
        return small
    else:
        return get_greatest_common_divisor_v2(big-small, small)

if __name__ == '__main__':
    print(get_greatest_common_divisor_v1(25,5))
    print(get_greatest_common_divisor_v1(100, 75))
    print(get_greatest_common_divisor_v1(99, 55))
    print(get_greatest_common_divisor_v1(7, 2))

    print('--------------')

    print(get_greatest_common_divisor_v2(25, 5))
    print(get_greatest_common_divisor_v2(100, 75))
    print(get_greatest_common_divisor_v2(99, 55))
    print(get_greatest_common_divisor_v2(7, 2))

