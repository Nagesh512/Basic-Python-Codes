count_even = 0
count_odd = 0
with open("Lecture 7/numbers.txt", "r") as f:
    data = f.read()
    print(data)
    
    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count_even +=1
        else:
            count_odd +=1

print(count_even)
print(count_odd)

count_even = 0
count_odd = 0

with open("Lecture 7/numbers2.txt", "r") as f:
    # .read().split() is magic: it splits by ANY whitespace (spaces, tabs, newlines)
    # Then we replace commas so we just have raw numbers
    data = f.read().replace(",", " ")
    nums = data.split()

    for val in nums:
        # Check if the string is actually a number before converting
        if val.isdigit():
            number = int(val)
            if number % 2 == 0:
                count_even += 1  # Fixed the += operator!
            else:
                count_odd += 1

print(f"Total Even: {count_even}")
print(f"Total Odd: {count_odd}")

# with open("Lecture 7/numbers.txt", "r") as f:
#     data = f.read()
#     print(data)

#     num = ""
#     for i in range(len(data)):
#         if (data[i] == "," ):
#             print(int(num))
#             num =""
#         else:
#             num += data[i]