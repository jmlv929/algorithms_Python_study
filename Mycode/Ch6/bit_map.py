'''

bitmap 位图算法
内存中连续的二进制位（bit）组成的数据结构 该算法主要用于对大量整数做去重和查询操作

占用内存少 且具有高性能的位运算
'''

#书中的位图是从0-9  这个位图是从0-size-1

class Bit_Map:
    def __init__(self, size):    #size 为输入ID总数 书中的 人 的标号
        self.size = size          #bitmap两个属性  分别为长度 以及存储的位   一个words元素 比如[0] 里面有64个bit
        self.words = [0] * (self.get_words_index(size-1)+1)    #这个地方非常巧妙 因为get_words_index返回的是一个整数 比如size=129 words =[0,0,0]
        #  self.words = [0] * (self.get_words_index(size))   错误！！  因为size=129  words=[0,0]  主要原因是 get_words_index 为整除 // 向下取整

    def get_words_index(self,index): #通过index得到所在words
        return index >> 6     #python中每个int 可以表示int 或者 长整形 移位 6位  等价于 index // 64 得到的还是一个整数

    def set_bit(self, index): #设置index 的bit为1
        word = self.get_words_index(index)  #得到index 对应的word  words=0  index 0-63
        self.words[word] |= 1<<index

    def get_bit(self,index):
        word = self.get_words_index(index)  # 得到index 对应的word  words=0  index 0-63
        bits = self.words[word] & (1<<index)
        # return bits[index]   TypeError: 'int' object is not subscriptable
        if bits == 0:
            return 0
        else:
            return 1


if __name__ == '__main__':
    my_bit_map = Bit_Map(129)
    my_bit_map.set_bit(75)
    my_bit_map.set_bit(127)

    print(my_bit_map.get_bit(127))
    print(my_bit_map.get_bit(74))
    print(my_bit_map.get_bit(76))
    print(my_bit_map.get_bit(75))






