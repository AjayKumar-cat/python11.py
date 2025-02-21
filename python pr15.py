# write a program to find whether a student has passed or failed in a subject. The program should take the marks of the student as input and print whether the student has passed or failed. A student has passed if the marks are greater than or equal to 40.

marks = int(input("Enter the marks of the student: "))
if(marks>=40):
    print("The student has passed")
else:
    print("The student has failed")


    # The program should take the marks of the student as 3 input and print whether the student has passed or failed. A student has passed if the marks are greater than or equal to 40%
     
marks1 = int(input("enter the marks of the student in subject1:"))
marks2 = int(input("enter the marks of the student in subject2:"))
marks3 = int(input("enter the marks of the student in subject3:"))

total_percentage = (marks1+marks2+marks3)/300

if(total_percentage>=40):

    print("The student has passed")
else:
    print("The student has failed")
    