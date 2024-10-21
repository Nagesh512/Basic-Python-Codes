# for loops are used for sequential traversal 
# For traversing list, string, tuple  etc

# list = [1, 2, 3, 4, 5, 6]
# for el in list:
#     print(el)


# veggies = ["potato", "brinjal", "flower", "onion"]
# for item in veggies:
#     print(item)


# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# for el in nums:
#     print(el)


# string = "ApnaCollege"
# for char in string:
#     print(char)


# string = "ApnaCollege"
# for char in string:
#     if(char == 'q'):
#         print("q found")
#         break
#     print(char)
# else :
#     print("q is not present in this string")


# list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# for el in list:
#     print(el)


tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
n = int(input("Enter a number"))
i = 0
for el in tuple:
    if(el == n):
        print(n , "is found at index", i)
        break
    i +=1
    
else:
    print("given number is not present in tuple")

