#Средствами языка Python сформировать текстовый файл (.txt), содержащий
#последовательность из целых положительных и отрицательных чисел. Сформировать
#новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
#обработку элементов:
#Исходные данные
#Количество элементов
#Минимальный элемент
#Числа кратные трем
#Количество чисел кратных трем

l = ['-99 6 12 -36 20 45 100 -15']
open("data1.txt","w").writelines(l)
open("data2.txt","w").write(f"Исходные данные: {l[0]}\nМинимальное число: {min([int(x) for x in l[0].split(' ')])}\nОбщее количество чисел: {len([int(x) for x in l[0].split(' ')])}\nКоличество чисел кратных 3-м: {len([i for i in [int(x) for x in l[0].split(' ')] if i % 3 == 0])}\nЧисла кратные 3-м: {str([i for i in [int(x) for x in l[0].split(' ')] if i % 3 == 0]).replace('[','').replace(']','')}")