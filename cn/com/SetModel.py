student = {"Tom", "Jim", "Mark", "Tom", "Jack", "Rose"}

print(student)

if 'Rose' in student:
    print("Rose在集合中")
else:
    print("Rose不在集合中")

a = set("abracadabra")
b = set("alacazam")

print(a)
print(b)

print(a - b)

print(a | b)

print(a & b)

print(a ^ b)
