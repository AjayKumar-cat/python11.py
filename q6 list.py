Friends =["apple","banana", 5 , 432.98 , False, "Ajay", "Vijay"]
print(Friends[0])
Friends[0] = "mango"# list are mutable
print(Friends[0])
Friends.append("yo yo")# add element at the end of the list append() method is used
print(Friends)

li = [11,5,7,99,44,23,56]
li.sort()# sort the list
print(li)


li = [11,5,7,99,44,23,56]
li.reverse()# reverse the list
print(li)

li = [11,5,7,99,44,23,56]
li.insert(2,7777)# insert 7777 at index 2
print(li)

li = [11,5,7,99,44,23,56]
li.pop(2)# remove element at index 2
print(li)

li = [11,5,7,99,44,23,56]
li.remove(44)# remove element 44
print(li)
