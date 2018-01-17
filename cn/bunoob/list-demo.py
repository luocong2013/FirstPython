list1 = ['Google', 'Runoob', 1997, 2000, 1997, 2000]
list2 = [1, 2, 3]
list3 = [4, 5, 6]

print(list1)

# 列表元素个数
print(len(list1))

# 删除列表元素
del list1[2]
print(list1)

# 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
list1.pop(1)
print(list1)

# 移除列表中某个值的第一个匹配项
list1.remove(2000)
print(list1)

# 在列表末尾添加新的对象
list1.append(1997)
print(list1)

# 将对象插入列表
list1.insert(1, 'Alibaba')
print(list1)

# 统计某个元素在列表中出现的次数
print(list1.count(1997))

# 从列表中找出某个值第一个匹配项的索引位置
print(list1.index(1997))

# 在列表末尾一次性追加另一个序列中的多个值
list2.extend({7, 8, 9})
print(list2)

# 返回列表元素最大值
print(max(list2))

# 返回列表元素最小值
print(min(list2))

# 反向列表中元素
list3.reverse()
print('反向列表中元素: ', list3)

# 对原列表进行排序
list3.sort()
print('对list3原列表进行排序: ', list3)

# 清空列表
list3.clear()
print('清空列表: ', list3)

# 复制列表
list3 = list2.copy()
print('复制列表: ', list3)

# +
print(list2 + list3)

# *
print(list2 * 3)

# 嵌套列表
print([list2, list3])
