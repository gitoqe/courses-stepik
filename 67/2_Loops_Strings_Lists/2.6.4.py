"""
Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк. После последней
строки матрицы идёт строка, содержащая только строку "end" (без кавычек, см. Sample Input).

Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме элементов первой
матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний элемент находится с
противоположной стороны матрицы.

В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.
"""


original_matrix = []

new_row = input()
while new_row != "end":
    new_row = new_row.split()
    new_row = [int(el) for el in new_row]
    original_matrix.append(new_row)
    new_row = input()

rows_num = len(original_matrix)
cols_num = len(original_matrix[0])
result_matrix = []

for row in range(0, rows_num):
    temp_row = []
    for el in range(0, cols_num):
        temp_el = original_matrix[row - 1][el] + \
                  original_matrix[(row + 1) % rows_num][el] + \
                  original_matrix[row][el - 1] + \
                  original_matrix[row][(el + 1) % cols_num]
        temp_row.append(temp_el)
    result_matrix.append(temp_row)

for row in range(0, rows_num):
    row_content = ''
    for el in range(0, cols_num):
        row_content += str(result_matrix[row][el]) + ' '
    print(row_content)
