# Write a recursive function to calculate the sum of first n natural numbers.

def sum(n):
    if(n==1):
        return 0
    return n + sum(n-1) 

print(sum(9))



# Write a recursive function to print all elements in a list.
# Hint : list & index as parameters.

list = ['a', 'b', 'c', 'd', 'e']

def ele_list(list , index = 0):
    if(len(list) == index):
        return
    print(list[index])
    ele_list(list, index+1)

ele_list(list)
