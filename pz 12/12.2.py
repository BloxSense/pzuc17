#Составить генератор (yield), который преобразует все буквенные символы в
#заглавные.

def to_upper(char):
    return char.upper() if char.isalpha() else char

def upper_functional(text):
    return ''.join(map(to_upper, text))

input_text = input("Введите символы: ")
result = upper_functional(input_text)
print(result)