'''4. Напишите программу, которая принимает 
на вход 2 числа. Задайте список из N элементов, 
заполненных числами из промежутка [-N, N]. 
Найдите произведение элементов на указанных 
позициях(не индексах).
Position one: 1
Position two: 3
Number of elements: 5
-> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
-> 15'''
num1 = int(input("Enter 1st number "))
num2 = int(input("Enter 2nd number "))
num1 *= -1

a = list(range(num1,num2+1))
b = len(a)
print(b)

pos1 = int(input('Enter the position of 1st number '))
pos2 = int(input("Enter the position of 2nd number "))

if (b >pos1) or (b<pos2):
    pos1 = pos1 - 1
    pos2 = pos2 -1
    e = a[pos1] * a[pos2]
    print(a)
    print(e)
else:
    print("list index out of range")