# del keyword
# Used to delete object properties or objects itself

class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Roonya")
print(s1.name)
del s1.name
print(s1.name)