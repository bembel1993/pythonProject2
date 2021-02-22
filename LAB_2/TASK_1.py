# 1. Реализуйте рекурсивную функцию нарезания прямоугольника с заданными
# пользователем сторонами a и b на квадраты с наибольшей возможной на каждом
# этапе стороной. Выведите длины ребер получаемых квадратов и кол-во
# полученных квадратов.

def squares(a, b, n = 0):
    if (a == b):
        return n + 1
    if (a < b):
        return squares(a, b - a, n + 1)
    if (a > b):
        return squares(a - b, b, n + 1)

a = int(input("Enter number --a--:"))
b = int(input("Enter number --b--:"))

print(a)
print(b)

print(squares(a, b))

