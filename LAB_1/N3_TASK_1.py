#Сформировать одномерный список целых чисел A, используя генератор случайных чисел (диапазон от 0 до 99).
# Размер списка n ввести с клавиатуры. В соответствии со своим вариантом написать программу по условию,
# представленному в таблице ниже.

# 1. Удалить элемент с введенным номером a.
import random

n = int(input("LIST INTEGER NUMBER 'A' :\n"))
mas = []
A = []
B = []
for i in range(n):
    c = random.randint(0, n)
    mas.append(c)
    A = mas[i]
    print(A)
print("----------------------------------")
for i in range(n):
    if 3<mas[i]<9:
        del mas[i]
        print("DELETE ELEMENTS OF ARRAYS")
        print(mas[i])