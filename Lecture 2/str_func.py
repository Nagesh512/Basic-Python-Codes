# String Functions
# str.endsWith("er.") #returns true if string ends with substr
str = "i am studying python from apna College"
print(str.endswith("python"))

# str.capitalize( ) #capitalizes 1st char
print(str.capitalize())
print(str)


print(str.replace("python" , "javascript"))

# str.find( word ) #returns 1st index of 1st occurrence
print(str.find("o"))
print(str.find('q'))
            
str.count("am") #counts the occurrence of substr in string
print(str.count('a'))