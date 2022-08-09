"""
Выведите таблицу размером n * n, заполненную числами от 1 до n^2 по спирали,
выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5):
"""

# n = int(input())
n = 5
print(n)

result = [[0 for i in range(0, n)] for j in range(0, n)]

for row in range(0, n):
    row_content = ''
    for el in range(0, n):
        row_content += str(result[row][el]) + ' '
    print(row_content)


