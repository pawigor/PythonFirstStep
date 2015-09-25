__author__ = 'z'

a = [int(i) for i in input().split()]

a.sort()

p = a[0]
k = 1
for c in a[1:]:
    if c == p:
        k += 1
    else:
        if k > 1:
            print(p, end=' ')
        p = c
        k = 1
if k > 1:
    print(p)
