__author__ = 'z'

a = int(input())
b = int(input())
n = 1
while n % a != 0 or n % b != 0:
    n += 1
print(n)
