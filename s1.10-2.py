__author__ = 'z'
y = int(input())
v = 'Високосный'
o = 'Обычный'
r = o
if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
    r = v

print(r)
