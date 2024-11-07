def product_of_elements(array):
    product = 1
    for num in array:
        product *= num
    return product
def average_of_elements(array):
    if len(array) == 0:
        return 0
    return sum(array) / len(array)
def main():
    array1 = list(map(int, input("Введите элементы первого массива через пробел:").split()))
    array2 = list(map(int, input("Введите элементы второго массива через пробел:").split()))
    array3 = list(map(int, input("Введите элементы третьего массива через пробел:").split()))
    for i, array in enumerate([array1, array2, array3], start=1):
        product = product_of_elements(array)
        average = average_of_elements(array)
        print(f"Массив {i}:")
        print(f"  Произведение элементов: {product}")
        print(f"  Среднее арифметическое: {average}")
if __name__ == "__main__":
    main()

