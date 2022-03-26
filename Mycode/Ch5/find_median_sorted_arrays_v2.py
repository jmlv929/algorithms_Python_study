


'''
题目叙述如v1所示


参考源文件 有点复杂  尤其是判断条件

'''


def find_median(a,b):
    length_a,length_b  = len(a),len(b)
    if length_a > length_b:   # 令数组a为长度较小的数组 防止利用二分法在数组a中寻找 数组b的index越界
        a,b,length_a,length_b = b,a,length_b,length_a
    if length_b < 0:
        raise Exception('给的数组出错了！')
    start,end = 0,length_a
    half_len = (length_a+length_b+1) // 2 # half_len 为大数组中排在橙色部分最左边的一个元素index

    while start <= end:  # i 的两边的范围再变  非常巧妙
        i = (start + end) // 2  #二分法
        j = half_len - i
        if i < length_a and b[j-1] > a[i]:
            start = i + 1  # i偏小 向右移动
        elif i > 0 and a[i-1] > b[j]:
            end = i - 1   #i偏大 向左移动
        else:
            # 处理特殊情况                 #特殊情况都放在一个 else 里面
            if i == 0:       # 数组a的长度小于数组b  且都大于数组b
                max_left = b[j-1]
            elif j == 0:
                max_left = a[i-1]
            else:
                max_left = max(a[i-1],b[j-1])
            if (length_a+length_b)%2 == 1:
                return max_left   # 大数组长度为奇数  返回左边最大值 不用计算右边最大值
            if i == length_a:
                min_right = b[j]
            elif j == length_b:
                min_right = a[i]
            else:
                min_right = min(a[i]+b[j])
            return (max_left+min_right)/2.0

if __name__ == '__main__':
    a = [3,5,6,7,8,15,20]
    b = [1,10,12,18,21,24,25,27]
    print(find_median(a,b))
