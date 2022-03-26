'''

状态转移方程式：
:param n 金矿数量
:param w 工人数量
:param p=[] 金矿开采所需人数
:param g=[] 金矿含金量

F(n,w) 为n个金矿 w个工人 最优收益函数

F(n,w) = 0 (n=0 || w=0)

F(n,w) = F(n-1,w) (w < p[n-1], n>= 1)  #工人数量小于当前金矿所需人数 不能挖当前金矿了  n-1为index p[n-1] 代表当前人数为n时金矿所需开采人数

F(n,w) = max(F(n-1,w), F(n-1,w-p[n-1]+g[n-1])  (n>= 1 and w >= p[n-1])

空间复杂度 时间复杂度 O(nw)

空间复杂度可以进一步降低  只能一个数组 从后向前开始更新 因为下一个每个元素只用到上一行的  F(n,w) = max(F(n-1,w), F(n-1,w-p[n-1]+g[n-1])  (n>= 1 and w >= p[n-1])
从后向前更新的原因为 后面元素要比较上一行中前面的元素
'''

#自底向上  动态规划 横轴为人数 纵轴为金矿 间距最小为一个人
def get_best_gold_mining_v1(w ,p ,g): #金矿数量由数组g可以得到
    F = [[0 for i in range(w+1)] for j in range(len(g)+1)]  # w+1个横轴 方便计算
    #填满表格
    for i in range(1,len(g)+1):  #堆数
        for j in range(1,w+1):  #人数
            if j < p[i-1]:    # 此时没有两个选择  只能不要当前这个金矿是最优选择 不要这个金矿 金矿-1
                F[i][j] = F[i-1][j]
            else:
                F[i][j] = max(F[i-1][j],F[i-1][j-p[i-1]]+g[i-1])
    return F[len(g)][w]

if __name__ == '__main__':
    w = 10
    p=[3,4,3,5,5]
    g=[200,300,350,400,500]
    print(get_best_gold_mining_v1(w,p,g))