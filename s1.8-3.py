__author__ = 'z'
min = int(input())
h = int(input())
m = int(input())
m_ = (min + h * 60 + m)
print(m_ // 60)
print(m_ % 60)
