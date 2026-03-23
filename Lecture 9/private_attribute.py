# Private(like) attributes & methods
# Conceptual Implementations in python
# Private attributes & methodsare meant to be used only within the class and
#  are not accessible from outside the class

# Public (Standard): Accessible from anywhere. Example: self.name

# Private (__): Accessible only inside the class methods. Example: self.__password

# The "Why": We use private attributes to protect sensitive data 
# (like a bank balance or password) 
# from being changed accidentally or maliciously by other parts of the program.

class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def show_password(self):
        # We CAN access private attributes inside the class
        print(f"Your password is: {self.__acc_pass}")
    
    def __hello(self):            # Private method
        print("Hello, this is a secret.")

    def welcome(self):
        self.__hello()

acc1 = Account(12345, "abcde")
print(acc1.acc_no)

# print(acc1.__acc_pass) -->this will gives error as make the variable as private so we can acces that inside the class only
acc1.show_password()

# acc1.__hello()  --> We are not able to access this also
acc1.welcome()