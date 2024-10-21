# Range functions returns a sequence of numbers, 
# starting from 0 by default, 
# and increments by 1 (by default), and stops before a specified number

# range( start?, stop, step?)

# seq = range(10)     # it saves by default 0 to 10 numbers(range property)
# for i in seq:
#     print(i)

# for i in range(10):    # range(stop)
#     print(i)

# for i in range(1, 10):      #range(start, stop)
#     print(i)


for i in range(2, 10 , 2):       #range(start, stop, step)
    print(i)

for i in range(1, 11):
    print(i *3)