#В последовательности на n целых элементов найти количество пар, для которых
#произведение элементов делится на 3 (элементы пары в последовательности являются
#соседними).

def count_pairs_divisible_by_3(sequence):
    count = sum(1 for x in range(len(sequence) - 1) if (sequence[x] * sequence[x-1]) % 3 == 0)
    return count

sequence = []
n = int(input("Введите количество чисел: "))
sequence = [int(input("Введите число: ")) for x in range(n)]

pairs_count = count_pairs_divisible_by_3(sequence)
print("Количество пар, произведение которых делится на 3:", pairs_count)