# Static method
# Method that don't use the self as parameter(work at class level)

class Student:
    college_name = "ABC College"
    
    def __init__(self, name, marks):
        self.name = name    
        self.marks = marks
    
    @staticmethod   # decorator
    def hello():
        print("Hello")

# *Decorators allow us to wrap another function in order to
# extend the behaviour of the wrapped function, without
# permanently modifying it

s1 = Student("karan", 97)
print(s1.name, s1.marks)
s1.hello()
