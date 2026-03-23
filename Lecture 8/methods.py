# Methods are functions that belongs to objects 

class Student:
    college_name = "ABC College"
    
    def __init__(self, name, marks):
        self.name = name    
        self.marks = marks
        print("Adding new student in Database")
    
    def welcome(self):
        print("Welcome Students, ", self.name)
    
    def get_marks(self):
        return self.marks

s1 = Student("karan", 97)
print(s1.name, s1.marks)
s1.welcome()
print(s1.get_marks())