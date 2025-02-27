# program using function to find greatest of three numbers.

num1 = int(input("enter the number 1:"))
num2 = int(input("enter the number 2:"))
num3 = int(input("enter the number 3:"))

def greatest( num1, num2, num3):
    if num1>num2 and num1>num3:
       print("num1 is gratest")
    if num2>num1 and num2>num3:
       print("num2 is greatest")
    else :
       print ("num3 is greatest")

greatest( num1, num2, num3)

# done by me❤️😍