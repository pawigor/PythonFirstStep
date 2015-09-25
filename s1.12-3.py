__author__ = 'z'
a = float(input())
b = float(input())
op = input()

if b == 0.0 and op in {"/", "mod", "div"}:
    print("Деление на 0!")
    exit(0)

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)
elif op == "mod":
    print(a % b)
elif op == "div":
    print(a // b)
elif op == "pow":
    print(a ** b)
