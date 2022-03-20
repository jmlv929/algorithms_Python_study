
'''

判断一个数是不是2的整数幂

对于一个整数n  如果 n&(n-1)的结果是0 就是
'''

def is_power_of_2(a):
    return (a & (a-1) == 0)

if __name__ == '__main__':
    print(is_power_of_2(8))
    print(is_power_of_2(9))
    print(is_power_of_2(64))