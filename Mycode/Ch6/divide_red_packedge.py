'''
抢红包 尽可能公平

'''

# 二倍均值法 每次随机金额的平均值是相等的  每次随机金额的上限定为剩余人均金额的2倍

# 每次抢到的金额 = 随机[0.01 - m/n*2-0.01]元  m剩余金额 n剩余人数
import random

def divide(m, n):
    red_packedge = [] # 存储每人得到的金额
    m *= 100
    for i in range(n-1):
        mount = random.randint(1,int(m/n)*2-1)   # print (random.randint(1, 10))  10  包括10
        red_packedge.append(mount)
        m -= mount
        n -= 1
    red_packedge.append(m)
    new_red_packedge = [i/100 for i in red_packedge]
    return new_red_packedge

if __name__ == "__main__":
    m = 100
    n =5
    print(divide(m, n))
