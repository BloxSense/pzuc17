def proverka(A, B):
    if A == 0 or B == 0:
        return 0

    side = min(A, B) #Нахождение наименьшей стороны

    return proverka(A - side, B) + proverka(A, B - side) + 1 #Вызываем функцию рекурсивно для оставшегося прямоугольника


A = int(input("Введи число:"))
B = int(input("Введи число:"))
result = proverka(A, B)
print(f"Можно разрезать на {result} квадратов.")
