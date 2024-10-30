a = []
b = []
print("Введите 10 элементов массива a:")
for _ in range(10):
    element = float(input())
    a.append(element)
print("Введите 10 элементов массива b:")
for _ in range(10):
    element = float(input())
    b.append(element)
print("Исходный массив a:", a)
print("Исходный массив b:", b)
a, b = b, a
print("Преобразованный массив a:", a)
print("Преобразованный массив b:", b)
