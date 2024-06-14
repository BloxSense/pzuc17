#В матрице элементы столбца N (N задать с клавиатуры) увеличить в два раза.
def input_matrix_dimensions():
    rows = int(input("Введите количество строк матрицы: "))
    cols = int(input("Введите количество столбцов матрицы: "))
    n = int(input("Введите номер столбца (отсчет начинается с 0), который нужно изменить: "))
    return rows, cols, n

def input_matrix(rows, cols):
    return [[float(input(f"Введите элемент матрицы [{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]

def modify_column(matrix, n):
    return [[row[j] * 2 if j == n else row[j] for j in range(len(row))] for row in matrix]

def main():
    rows, cols, n = input_matrix_dimensions()
    matrix = input_matrix(rows, cols)
    modified_matrix = modify_column(matrix, n)
    print("Измененная матрица:")
    for row in modified_matrix:
        print(row)

if __name__ == "__main__":
    main()