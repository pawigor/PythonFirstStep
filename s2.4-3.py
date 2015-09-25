__author__ = 'z'

s = input()
k = 0

for c in s.upper():
    if c == 'G' or c == 'C':
        k += 1

print(k / len(s) * 100)
