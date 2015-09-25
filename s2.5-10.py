__author__ = 'z'

a = [int(i) for i in input().split()]
if len(a) == 1:
    print(a[0])
else:
    for index in range(len(a)):
        if index == len(a) - 1:
            print(a[index - 1] + a[(index + 1) % len(a)])
        else:
            print(a[index - 1] + a[(index + 1) % len(a)], end=' ')
