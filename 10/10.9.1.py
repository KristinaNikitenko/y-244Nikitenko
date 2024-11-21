def find_A_and_max(lst, k):
    A=[]
    for row in lst:
        for elem in row:
            if elem % k==0:
                A.append(elem)
    if A:
        return len(A), max(A)
    else:
        return 0, None
with open('C:\\pyton\\10\\Никитенко_У-244_vvod.txt', 'r') as file:
    lst = file.readlines()
lst = [[float(n) for n in x.split()] for x in lst]
print(lst)

k=int(input("Введите число k: "))
num_A, max_A = find_A_and_max(lst, k)
str1 = "Количество элементов, кратных " + str(k) + ": " + str(num_A) + "\n"
str2 = "Наибольший элемент, кратных " + str(k) + ": " + str(max_A)
with open('C:\\pyton\\10\\Никитенко_У-244_vivod.txt', 'w') as file1:
    file1.write(str1)
    file1.write(str2)
print(str1)
print(str2)


