num = int(input("Enter a number to find odd or even\n"))

if(num % 2 == 0):
    print("Given number is an even number")
else:
    print("Given number is an odd number")


num1 = int(input("Enter three numbers\n"))
num2 = int(input())
num3 = int(input())

if(num1 > num2 and num1 > num3):
    print(num1 , "is the gretest amongst three")
elif(num2 > num1 and num2 > num3):
    print(num2 , "is the gretest amongst three")
else:
    print(num3 , "is the gretest amongst three")



num7 = int(input("Enter a number then i will check it is multiple of 7 or not : "))
if(num % 7 == 0):
    print(num7, " is multiple of 7")
else:
    print(num7, " is not multiple of 7")