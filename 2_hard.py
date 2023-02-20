"""
Сгенерировать массив случайных целых чисел размерностью m*n (размерность вводим с клавиатуры) , 
причем чтоб количество элементов было четное. Вывести на экран красивенько таблицей.
Перемешать случайным образом элементы массива, причем чтобы каждый гарантированно и 
только один раз переместился на другое место и выполнить это за m*n / 2 итераций.
 То есть если массив три на четыре, то надо выполнить не более 6 итераций. И далее в конце опять вывести на экран как таблицу.
"""
from random import randint

a = []
b = []
c = []

while True:
    n = int(input("введите колво строк "))
    m = int(input("введите колво столбцов "))
    if m*n%2 == 0:
        for i in range(0,n):   
            a.append([0]*m)
        break
    else:
        print("Колво элементов должно быть четным")
        continue


for i in range(0,n):
    for j in range(0,m):
        a[i][j] = randint(1,9)

for i in range(0,n):
    for j in range(0,m):
        print(a[i][j],end = ' ')
    print()

for i in range(0,n):
    for j in range(0,m):
        b.append(a[i][j])

for i in range(0,n):
    c.append([0]*m)

i = 0
j = 0
count = 0
print()

while len(b)!=0:
    rand = randint(len(b)//2,len(b)-1)
    temp = a[i][j]
    a[i][j] = b.pop(rand)
    a[rand//m][rand-(rand//m)*m] = temp
    b.remove(temp)
    j+=1
    if j==m:
        i+=1
        j=0
    count+=1

for i in range(0,n):
    for j in range(0,m):
        print(a[i][j],end = ' ')
    print()

    
print(f"Колво итераций:{count}")






