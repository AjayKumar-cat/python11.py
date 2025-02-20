e = set() # dont use {} to create empty set because it will create empty dictionary

s = {1, 3 ,44, 5, 6, 8, 9, 10, 11, 13, 15}

print(s, type(s))
s.add(100)# add element to the set
print(s)
s.remove(100)# remove element from the set
print(s)
s.pop()# remove random element from the set
print(s)
s.clear()# remove all the elements from the set
print(s)

