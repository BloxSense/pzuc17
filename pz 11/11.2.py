#Из предложенного текстового файла (text18-20.txt) вывести на экран его содержимое,
#количество символов в тексте. Сформировать новый файл, в который поместить строку
#наибольшей длины.

text = open("Text.txt",'r',encoding="utf-16")
longest_line = ""
all_text = ""
symbol_count = 0
for line in text.readlines():
    if len(line) > len(longest_line):
        longest_line = line
    for i in line:
        symbol_count += 1
    all_text += line

print(f"Колличество символов: {symbol_count}\n".replace("'", ""),all_text)
open('LongestLine.txt',"w").write(longest_line)