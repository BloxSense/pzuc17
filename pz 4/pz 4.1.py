#Дано вещественное число X и целое число N (> 0). Найти значение выражения 1 -X^2/(2!) + X^4/(4!) - ... + (-1)^N-X^2*N/((2-N)!) (N! = 12 ...N). Полученное число является
#приближенным значением функции cos в точке X.

import math

def approximate_sin(x, n):
    result = 0

    for i in range(n):
        term = ((-1) ** i) * (x ** (2 * i + 1)) / math.factorial(2 * i + 1)
        result += term

    return result

# Ввод значений X и N
x = float(input("Введите вещественное число X: "))
n = int(input("Введите целое число N (> 0): "))

# Проверка на положительное значение N
if n <= 0:
    print("Пожалуйста, введите целое число N (> 0).")
else:
    approx_sin_value = approximate_sin(x, n)
    print(f"Приближенное значение sin({x}) с использованием {n} членов ряда Тейлора: {approx_sin_value}")
