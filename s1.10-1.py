__author__ = 'z'
a=int(input())
b=int(input())
h=int(input())
if h>b:
    print('Пересып')
elif h<a:
    print('Недосып')
elif h<=b and h>=a:
    print('Это нормально')