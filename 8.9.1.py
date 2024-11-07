def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def steps_to_zero(n):
    count = 0
    while n > 0:
        n -= sum_of_digits(n)
        count += 1
    return count
number = int(input("Введите число: "))
result = steps_to_zero(number)
print(f"Количество шагов до достижения нуля: {result}")
