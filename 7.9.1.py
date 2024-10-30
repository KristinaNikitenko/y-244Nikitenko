n = int(input("Введите количество элементов в массиве: "))
array = []
for i in range(n):
    element = float(input(f"Введите {i+1} элемент:"))
    array.append(element)
min_element = min(array, key=abs)
print(f"Минимальный по модулю элемент: {min_element}")
reversed_array = list(reversed(array))
print("Массив в обратном порядке:")
print(reversed_array)
