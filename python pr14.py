 # program to find greatest of four numbers  entered  by the user

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
d = int(input("Enter the fourth number: "))

if(a>b and a>c and a>d):
    print(a, "is the greatest number")
elif(b>c and b>d):
    print(b, "is the greatest number")
elif(c>d):
    print(c, "is the greatest number")
else:
    print(d, "is the greatest number")
print("End of Program")
