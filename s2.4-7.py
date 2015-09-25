__author__ = 'z'

s = input()

p = s[0]
k = 1
for c in s[1:]:
    if c == p:
        k += 1
    else:
        print(p, end='')
        print(k, end='')
        p = c
        k = 1
print(p, end='')
print(k, end='')
