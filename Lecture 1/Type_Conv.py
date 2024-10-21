# type Conversion  -- done automatically

a = 2
b = 4.2

sum = a + b  

# type casting -- done manually or forcefully
a = "2"
num = a 
print(type(num))
# sum = num + 1    this will give error
num = int(a)
sum = b + num
print(type(num))
print(type(sum))
