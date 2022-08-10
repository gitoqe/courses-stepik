"""
Выведите таблицу размером n * n, заполненную числами от 1 до n^2 по спирали,
выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5):
"""


def compare_2_arrays(array_1, array_2):
    print('\ncompare_2_arrays')
    n = len(array_1)
    temp_array = []
    for row in range(0, n):
        temp_row = []
        for el in range(0, n):
            if array_1[row][el] == array_2[row][el]:
                temp_row.append(True)
            else:
                temp_row.append(False)
        temp_array.append(temp_row)
        print(temp_row)


def print_array(array):
    print('\nprint_array')
    n = len(array)
    for row in range(0, n):
        row_content = ''
        for el in range(0, n):
            row_content += str(result[row][el]) + ' '
        print(row_content)

# n = int(input())
n = 5
print(n)

result = [[0 for i in range(0, n)] for j in range(0, n)]

print_array(result)

for row in range(0, n):
    for el in range(0, n):
        if row == el == 0:
            result[row][el] = 1
        else:
            result[row][el] = 1

print_array(result)

compare_2_arrays(result,
                 [[ 1,  2,  3,  4, 5],
                  [16, 17, 18, 19, 6],
                  [15, 24, 25, 20, 7],
                  [14, 23, 22, 21, 8],
                  [13, 12, 11, 10, 9]]
                 )
