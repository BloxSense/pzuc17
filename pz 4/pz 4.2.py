#Дано целое число N (> 0). Найти сумму 1^1 + 2^2 + ... + N^N


def calculate_sum(N):
    result = sum(i**i for i in range(1, N + 1))
    return result

# Пример использования
N = int(input("Введите целое число N (> 0): "))

# Проверка на положительное значение N
if N <= 0:
    print("Пожалуйста, введите целое число N (> 0).")
else:
    sum_result = calculate_sum(N)
    print(f"Сумма 1^1 + 2^2 + ... + N^N для N={N}: {sum_result}")
