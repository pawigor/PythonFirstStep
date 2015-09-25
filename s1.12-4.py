from math import sqrt

__author__ = 'z'

s = input()

pi = 3.14

if s == "треугольник":
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c) / 2
    S = sqrt(p * (p - a) * (p - b) * (p - c))
elif s == "прямоугольник":
    a = float(input())
    b = float(input())
    S = a * b
elif s == "круг":
    r = float(input())
    S = pi * r ** 2

print(S)
