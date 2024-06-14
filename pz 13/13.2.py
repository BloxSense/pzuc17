#В матрице элементы последней строки заменить на 0.
def replace_last_row_with_zeros(matrix):
    last_row_index = len(matrix) - 1
    return [ [0 if row == matrix[last_row_index] else value for value in row] for row in matrix]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix = replace_last_row_with_zeros(matrix)

for row in matrix:
    print(row)