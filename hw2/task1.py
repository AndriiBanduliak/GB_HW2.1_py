'''1. Напишите программу, которая принимает на
вход вещественное число и показывает сумму его цифр.
 6782 -> 23
- 0.67 -> 13
- 198.45 -> 27'''

a = float(input('enter the num: '))

suma = 0
a = a*1000000

if a < 0 :
    a = a *(-1)
    while a>0:
        s = a % 10
        suma +=s
        a = a//10
else:
    while a>0:
        s = a % 10
        suma +=s
        a = a//10

print(int(suma))