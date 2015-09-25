__author__ = 'z'

n = int(input())
programmer = "программист"
if n % 10 == 1 and n % 100 not in {11}:
    suffix = ""
elif n % 10 in {2, 3, 4} and n % 100 not in {12, 13, 14}:
    suffix = "а"
else:
    suffix = "ов"

print(n, programmer + suffix)
