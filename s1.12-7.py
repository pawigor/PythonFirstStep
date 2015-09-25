__author__ = 'z'

# "Счастливый" или "Обычный"

s = input()

v1 = int(s[0]) + int(s[1]) + int(s[2])
v2 = int(s[3]) + int(s[4]) + int(s[5])
if v1 == v2:
    print("Счастливый")
else:
    print("Обычный")
