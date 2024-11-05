# WAF to print the length of a list. ( list is the parameter)

# cities = ["pune", "nanded", "kolhapur", "mumbai", "nashik"]
# def len_list(list):
#     length = len(list)
#     print(length)
#     return length

# len_list(cities)



# WAF to print the elements of a list in a single line. ( list is the parameter)
# cities = ["pune", "nanded", "kolhapur", "mumbai", "nashik"]

# def print_ele(list):
#     for el in list:
#         print(el , end=" ")

# print_ele(cities)


# WAF to find the factorial of n. (n is the parameter)
# num = 4

# def fact(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     print(fact)

# fact(num)


# WAF to convert USD to INR.
inr = int(input("Enter USD "))

def doller_to_inr(usd):
    inr = 83.5 * usd
    print(usd  ,"USD = ", inr)

doller_to_inr(inr)
