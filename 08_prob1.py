# print multiplication table of input number given by user using for loop

n = int(input("Enter a number: "))
for i in range(1,11):
    print(
        f"{n} x {i} = {n*i}"
    )

