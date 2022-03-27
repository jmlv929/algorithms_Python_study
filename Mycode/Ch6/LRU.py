'''

LRU:Last Recently Used 内存管理算法

Pyhton中的collections.OrderedDict对 哈希链表 做了很好的实现 =>  让字典有序

'''


# 将类OrderedDict实例化会得到一个dict子类的实例，支持通常的dict方法。
from collections import OrderedDict

od=OrderedDict()

print(isinstance(od,OrderedDict)) # True
print(isinstance(od,dict)) # True

# OrderedDict是记住键首次插入顺序的字典。如果新条目覆盖现有条目，则原始插入位置保持不变。
od['name'] = 'egon'
od['age'] = 18
od['gender'] = 'male'
print(od) # OrderedDict([('name', 'egon'), ('age', 18), ('gender', 'male')])

od['age']=19
print(od) # OrderedDict([('name', 'egon'), ('age', 19), ('gender', 'male')])


# 删除条目并重新插入会将其移动到末尾。
del od['age']

od['age']=20
print(od) # OrderedDict([('name', 'egon'), ('gender', 'male'), ('age', 20)])

# 方法popitem(last=True)
# 调用有序字典的popitem()方法会删除并返回(key, value)对。如果last为真，
# 则以LIFO(后进先出)顺序返回这些键值对，如果为假，则以FIFO(先进先出)顺序返回。

print(od.popitem(last=True))  #LIFO  ('age', 20)
print(od.popitem(last=False))  # FIFO   ('name', 'egon')

# 方法move_to_end(key, last=True)
# 该方法用于将一个已存在的key移动到有序字典的任一端。如果last为True（默认值），
# 则移动到末尾，如果last为False，则移动到开头。如果key不存在，引发KeyError
print(od)  # OrderedDict([('gender', 'male')])
od['age'] = 20
od['school'] = 'xxx'
print(od)  # OrderedDict([('gender', 'male'), ('age', 20), ('school', 'xxx')])
od.move_to_end('age')
print(od)   # OrderedDict([('gender', 'male'), ('school', 'xxx'), ('age', 20)])