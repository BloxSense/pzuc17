#Проверить истинность высказывания: «Среди трех данных целых чисел есть хотя бы
#одна пара взаимно противоположных».

a = int(input("Введи число:"))
b = int(input("Введи число:"))
c = int(input("Введи число:"))

if a == -b or a == -c or b == -c:
    print("True")
else:
    print("False")