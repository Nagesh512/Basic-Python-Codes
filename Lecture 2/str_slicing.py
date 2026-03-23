# Slicing   

# str[ starting_idx : ending_idx ] #ending idx is not included
# string[start : stop : step]  step is optional


# Accessing parts of a string
str ='ApnaCollege'
print(str[ 1 : 4 ]) 

print(str[ : 4 ])

print(str[ 1 : ])

# negative index
#  P   Y   T   H   O   N
# -6  -5  -4  -3  -2  -1


str = "apple"
print(str[:-3])   
print(str[-6:-3])   

print(str[0:len(str):2])