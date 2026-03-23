
# Constructor 
# All classes have a function called  __init__()  
# which is always executed when the class is been initiated 

# The self parameter is a reference to the current
# instance of the class, and is used to access variables
# that belongs to the class.

class Student:

    # Default Constructor
    def __init__(self):
        pass

    college_name = "ABC college"
    # Parameterized Constructor
    def __init__(self, name, marks):
        self.name = name 
        self.marks = marks
        print("Adding new student in Database")

s1 = Student("karan", 97)
print(s1.name, s1.marks)

s2 = Student("Arjun", 92)
print(s2.name, s2.marks)

print(s2.college_name)
 