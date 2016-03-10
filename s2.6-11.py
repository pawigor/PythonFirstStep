# Выведите таблицу размером n×n, заполненную числами от 1 до n2 по спирали, выходящей из левого верхнего угла и
# закрученной по часовой стрелке, как показано в примере (здесь n=5):
#
# Sample Input:
#
# 5
#
# Sample Output:
#
# 1 2 3 4 5
# 16 17 18 19 6
# 15 24 25 20 7
# 14 23 22 21 8
# 13 12 11 10 9

n = int(input())
dx, dy = 0, 1
x, y = 0, 0
l = [[0] * n for i in range(n)]
for j in range(0, n ** 2):
    l[x][y] = j + 1
    nx, ny = x + dx, y + dy
    if 0 <= nx < n and n > ny >= 0 == l[nx][ny]:
        x, y = nx, ny
    else:
        dx, dy = dy, -dx
        x, y = x + dx, y + dy

for i in range(n):
    for j in range(n):
        print(l[i][j], end=' ')
    print()
