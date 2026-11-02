def print_hi(name):
 print(f'Hi, {name}')
if __name__ == '__main__':
    print_hi('PyCharm')

from random import *

n = int(input("введите количество элементов массива n: "))
a = float(input("введите начало интервала a: "))
b = float(input("введите конец интервала b: "))

mas = []
for i in range(n):

    chislo = uniform(-10, 10)
    mas.append(round(chislo, 2))

print("Исходный массив:", mas)

min_abs = abs(mas[0])
min_index = 0

for i in range(1, n):
    if abs(mas[i]) < min_abs:
        min_abs = abs(mas[i])
        min_index = i

print("номер минимального по модулю элемента:", min_index + 1)

summa = 0
nasli_otricatelniy = False

for i in range(n):
    if nasli_otricatelniy == True:
        summa = summa + abs(mas[i])

    if mas[i] < 0:
        nasli_otricatelniy = True

print("сумма модулей после первого отрицательного:", round(summa, 2))


j = 0
for i in range(n):

    if mas[i] < a or mas[i] > b:
        mas[j] = mas[i]
        j = j + 1

for i in range(j, n):
    mas[i] = 0

print("Массив после сжатия:", mas)