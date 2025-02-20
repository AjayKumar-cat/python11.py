marks = {
    "student1": 24,
    "student2": 30,
    "student3": 29
}
print(marks.items()) #use of items() method
print(marks.keys())#use to get keys
print(marks.values())#use to get values
marks.update({"student3": 31, "student4":99})#used to update the dictionary
print(marks)
print(marks.get("student1"))# used to get the value of the key