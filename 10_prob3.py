# print multiplication table of input number given by user using while loop

n = int(input("Enter a number: "))
i = 1
while(i<11):
    print(
        f"{n} x {i} = {n*i}"
    )
    i = i + 1