from random import randint as r

my_int = int(input("Enter the count of numbers in array "))

my_list = list(range(0,my_int+1))
print(my_list)
a = []

for i in my_list:
    a.insert(r(0,len(my_list)), i)

print(a)
