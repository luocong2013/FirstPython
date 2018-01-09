list = ["abcd", 789, 2.23, "runoob", 70.2]
tinylist = [123, "runoob"]

print(list)
print(len(list))
list.append('Admin')
list.insert(1, 'Jack')
list.pop(0)

print(list[0])
print(list[1:3])
print(list[2:])
print(tinylist * 2)
print(list + tinylist)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])
