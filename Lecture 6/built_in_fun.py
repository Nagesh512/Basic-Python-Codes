# Built in Functions

# print()
# len()
# type()
# range()

print("Nagesh" , end = " ")    
#end =" "   --> it will gives an space because in print function end is by default declare as end ="\n"
print("Salunke")

# User defined functions  --> are those functions which are declared by an user



#Default parameter -->
# Assigning a default value to parameter, which is used when no argument is passed.

def cal_prod(a=1, b =2):      #we are giving by default values
# def cal_prod(a=1, b):      #if we give default value to the first parameter then it will shows an error
#because default values should be give from the last parameter
    print(a * b)
    return a* b



