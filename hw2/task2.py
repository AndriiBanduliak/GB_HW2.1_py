'''2. Напишите программу, которая принимает на вход число N 
и выдает набор произведений чисел от 1 до N.
1 - 1 * 1, 2 - 1 * 2, 3 - 1 * 2 * 3, 4 - 1 * 2 * 3 * 4 и т.д.
- 4 -> [1, 2, 6, 24]
- 6 -> [1, 2, 6, 24, 120, 720]'''


# Второй вариант решения задачи № 2

n = int(input("Enter the number "))

f = 1

for i in range(1, n+1):
    f *=i
    print("The factorial of ",i," is", f)
