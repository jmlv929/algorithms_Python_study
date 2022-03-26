'''

一个无序数组里有若干个整数 范围是1-100 其中有98个证书出现了偶数次
只有两个整数出现了奇数次 如何找到这两个出现奇数次的整数？

异或运算满足 交换律 和 结合律

如果只有一个奇数次出现 将所有元素异或就可以

两个的话 就需要分治法 把这两个数放在不同组合 分开异或
'''

def find_lost_num(array=[]):
    result = [0,0]
    xor_result = 0
    A,B = [],[]

    for i in range(len(array)):
        xor_result ^= array[i]
    if xor_result == 0:
        raise Exception('不符合题意')
    flag = 1
    while xor_result & flag == 0:
        flag <<= 1  #找到位为1的index
    for i in array:
        if flag & i == 0:
            A.append(i)
        else:
            B.append(i)  #分成A和B两组
    for i in A:
        result[0] ^= i
    for i in B:
        result[1] ^= i
    return result

if __name__ == "__main__":
    my_array = [4,1,2,2,5,1,4,3]   #  3  5
    print(find_lost_num(my_array))

