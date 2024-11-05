# Function
# Block of statements that perform a specific task


# Function defination    -->def func_name()
def calc_sum(a, b): # paramaters  --> a & b are the parameters 
    return a+b


calc_sum(1, 3)    #call function   --> func_name(arg1, arg2)


def print_Hello():
    print("Hello")

print_Hello()
print_Hello()
print_Hello()
print_Hello()

# Function which has no return value -->if we store in any variable it will return --> None
output = print_Hello()
print(output)

def calc_avg(a, b , c):
    sum = a + b+ c
    avg = sum/3
    print(avg)
    return avg


