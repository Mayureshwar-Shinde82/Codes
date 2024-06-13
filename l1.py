a = [1,2,3,4,5,6,7,8,9,10]
print(list(a))

# Append : means it add element in last index of the list
b= [11,12,13]
a.append(b)
print(a)

# extend : it extend the list in the last 
c = [14,15,16]
a.extend(c)
print(a)

# insert or index : it insert element in the list at specig=fic index
a.insert(0,0)
print(a)

# remove : remove the element at from list
a.remove(16)
print(a)

# pop : it delete element in list at specific index
a.pop(0)
print(a)

# #clear : it delete all the elements int the list
# a.clear()
# print(a)

# count : it counts the occurances of given element
q = a.count(4)
print(q)

# index : It return the index of given element
print(a.index(15))

# reverse : It reverse the give list
a.reverse()
print(a)

# sort : It sorting the list If string Alphabetically else Ascending order
l = ["g",'r','r','t','z']
l.sort()
print(l)

# copy : It copy the list to another variable
d = a.copy()
print(d)

# __add__() : add the element in list 
e = a.__add__([16])
print(e)

# __len__ : give the length of list
print(a.__len__())


print(a.__repr__())

print(a.__rmul__(2))

print(a.__sizeof__()," bytes")