# program to detect the following spam comments:
# 1. make a lot of money,2. buy now,3. subscribe this,4. click this.

p1 = "make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

message = input("Enter your message: ")
if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("The message is a spam")

else : 
    print("The message is not a spam")  