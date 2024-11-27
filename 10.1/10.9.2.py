def find_max_and_reduce_matrix(matrix):
    assert len(matrix) == len(matrix[0])
    max_val = matrix[0][0]
    max_i = 0
    max_j = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if abs(matrix[i][j]) > abs(max_val):
                max_val = matrix[i][j]
                max_i = i
                max_j = j
    print("Наибольший по модулю элемент:", max_val)
    str1 = "Максимальный по модулю элемент: " + str(max_val) + "\n"
    with open('C:\\pyton\\10.1\\Никитенко_У-244_vivod.txt', 'w') as file1:
        file1.write(str1)
    new_matrix = [row[:max_j] + row[max_j+1:] for i, row in enumerate(matrix) if i != max_i]
    return new_matrix 
matrix = [[1, 2, 3], [4, -5, 6], [7, 8, 9]]
print("Исходная матрица:")
for row in matrix:
    print(row)
new_matrix = find_max_and_reduce_matrix(matrix)
print("Новая матрица:")
with open('C:\\pyton\\10.1\\Никитенко_У-244_vivod.txt', 'a') as file1:
    str2 = "Новая матрица: " + "\n"
    file1.write(str2)
    for row in new_matrix:
        print(row)
        file1.write(' '.join([str(a) for a in row]) + '\n')


