# i = 1
# while(i<=100):
#     print(i)
#     i += 1

# i=100
# while(i>=1):
#     print(i)
#     i -=1

# i=1
# n = int(input("Enter a number "))
# while(i<=10):
#     print(i * n)
#     i +=1

i=1
list =[]
while(i<=10):
    list.append(i*i) 
    i +=1
print(list)



nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
n = 36
i = 0
while(i < len(nums)):
    if(nums[i] == n):
        print(n ,"is present at index : " ,i)
        break
    else:
        print("finding....")
    i +=1

    

