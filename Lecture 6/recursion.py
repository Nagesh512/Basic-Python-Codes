# Recursion
# When a function calls itself repeatedly
# work which is done by loops can be done by using recursions also and vice versa

# Recursive Function

def show(n):
    if(n == 0):      #Base case --> if we not give then it will run infinitely
        return
    print(n)
    show(n-1)

show(10)


def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * fact(n-1)
    
print(fact(5))