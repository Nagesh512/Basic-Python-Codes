# List Methods
list = [2, 1, 3]
list.reverse()
print(list)

list.append(4) #adds one element at the end
print(list)

list.sort( ) #sorts in ascending order
print(list) 

list.sort( reverse=True ) #sorts in descending order
print(list)

# list.insert( idx, el ) #insert element at index
list.insert(2 , 8)
print(list)

list.remove(1) #removes first occurrence of element
print(list)


# list.pop( idx ) #removes element at idx
list.pop(2)
print(list)

list.count()

[1, 2, 3]
[2, 1, 3, 4]
[3, 2, 1]
