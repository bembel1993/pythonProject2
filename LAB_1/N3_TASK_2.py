#Сформировать одномерный список целых чисел A, используя генератор случайных чисел (диапазон от 0 до 99).
# Размер списка n ввести с клавиатуры. В соответствии со своим вариантом написать программу по условию,
# представленному в таблице ниже.

# 2. Все четные по значению элементы исходного списка A поместить в новый список B.
import random

n = int(input("LIST INTEGER NUMBER 'A' :\n"))
mas = []
B = []
for i in range(n):
    c = random.randint(0, n)
    mas.append(c)
    print(mas[i])
print("------------------------------")
print(" LIST INTEGER NUMBER 'B' :")
for i in range(n):
    if mas[i]%2 == 0:
        B = mas[i]
        print(B)


