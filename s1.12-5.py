__author__ = 'z'
a = int(input())
b = int(input())
c = int(input())

c_ = [a, b, c]
max = max(c_)
print(max)
min = min(c_)
print(min)
c_.remove(max)
c_.remove(min)
print(c_[0])
