collection = set()

collection.add(1)
collection.add(2)
collection.add(3)
collection.add((4,5,6))

print(collection)

collection.remove(2)
print(collection)
print(len(collection))

collection.clear()
print(collection)



Collection = {1, "Hello", 2 , 5, "World"}
Collection.pop() #we cannot write it without print function
print(Collection)     


#Unhashable value(values can be change or mutable) --> immutable value   (tuple, set)
# Hashable value  --> mutable value(list, dictionary)

set1 = {1, 2 , 3 ,5}
set2 = {6, 7, 9, 1, 2}

print(set1.union(set2))
print(set1.intersection(set2))