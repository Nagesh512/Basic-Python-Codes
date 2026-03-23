# Property


class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

        self.percentage = str((self.phy + self.chem + self.math)/3) + "%"
        # This will not reflect the changes if we change the value of specific attributes

    def calc_percentage(self):
        self.percentage = str((self.phy + self.chem + self.math)/3) + "%"

    

s1 = Student(89, 98, 99)
print(s1.percentage)

s1.phy = 69
print(s1.phy)
print(s1.percentage)  # this will not reflex the changes directly 

s1.calc_percentage()  # we runthese first then only we will gwt the correct output
print(s1.percentage)

print()
         

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math)/3) + "%"
    

s1 = Student(89, 98, 99)
print(s1.percentage)

s1.phy = 69
print(s1.phy)
print(s1.percentage)