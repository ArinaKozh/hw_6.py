"""
Задайте двумерный массив из целых чисел. Количество строк и столбцов задается с клавиатуры.
Отсортировать элементы по возрастанию слева направо и сверху вниз.

Например, задан массив:
1 4 7 2
5 9 10 3

После сортировки
1 2 3 4
5 7 9 10
"""
from random import randint

n = int(input("введите колво строк "))
m = int(input("введите колво столбцов "))
a = []
b = []
for i in range(0,n):
    a.append([0]*m)

for i in range(0,n):
    for j in range(0,m):
        a[i][j] = randint(1,9)
print(a)


for i in range(0,n):
    for j in range(0,m):
        b.append(a[i][j])
for k in range(m*n):
    for i in range(0,n*m-1):
        if b[i]>b[i+1]:
            temp = b[i]
            b[i] = b[i+1]
            b[i+1] = temp
for i in range(0,n):
    for j in range(0,m):
        a[i][j] = b[i*m+j]


print(a)






