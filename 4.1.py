a = int(input("Введите целое число a: "))
b = int(input("Введите целое число b (a <= b): "))
if a <= b:
    print(f"Целые числа от {a} до {b} включительно:")
    for i in range(a, b + 1):
        print(i, end=';')
else:
    print("Ошибка: a должно быть меньше или равно b.")