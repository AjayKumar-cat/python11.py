# Write a program to print the multiplication table of a given number in reverse order.
n = int(input("Enter the number: "))

for i in range(1, 11):
    print(f"{n} X {11 -i} = {n*(11-i)}")