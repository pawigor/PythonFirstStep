__author__ = 'z'


# Напишите функцию f(x), которая возвращает значение следующей функции, определённой на всей числовой прямой:
#
# f(x)=⎧⎩⎨⎪⎪1−(x+2)2,−x2,(x−2)2+1,при x≤−2при −2<x≤2при 2<x
# f(x)={1−(x+2)2,при x≤−2−x2,при −2<x≤2(x−2)2+1,при 2<x
# Требуется реализовать только функцию, решение не должно осуществлять операций ввода-вывода.

def f(x):
    result = 0
    if x <= -2:
        result = 1 - (x + 2) ** 2
    elif -2 < x <= 2:
        result = -x / 2
    elif x > 2:
        result = (x - 2) ** 2 + 1

    return result


print(f(4.5))
print(f(-4.5))
print(f(1))
