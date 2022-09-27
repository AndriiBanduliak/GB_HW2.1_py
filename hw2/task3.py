'''3. Задайте список из n чисел, заполненный по формуле 
(1 + 1/n) ** n и
выведите на экран их сумму.
Для n = 6: [2, 2, 2, 2, 2, 3] -> 13'''

a_int = int(input("Enter the number: "))

int_list = []

for i in range(1, a_int + 1):
    int_list.append( int(round( ( (1 + 1/i) ** i), 0)))
 
print(f"For n = {a_int}: {int_list} -> {sum(int_list)}")