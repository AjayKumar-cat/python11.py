# program to find whether a given username is less than 10 characters or not.

username = input("Enter the username: ")
if(len(username)<10):
    print("The username is less than 10 characters")
else:
    print("The username is greater than 10 characters")
    
print("End of Program")

print(len(username))