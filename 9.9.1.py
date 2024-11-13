def find_A_and_max(matrix, k):
    A=[]
    for row in matrix:
        for elem in row:
            if elem % k==0:
                A.append(elem)
    if A:
        return len(A), max(A)
    else:
        return 0, None
matrix = [[10, 20, 30], [45, 55, 65], [70, 80, 90]]
k=int(input("Введите число k: "))
num_A, max_A = find_A_and_max(matrix, k)
print(f"Количество элементов, кратных {k}: {num_A}")
print(f"Наибольший элемент, кратный {k}: {max_A}")