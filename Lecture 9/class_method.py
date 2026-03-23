# class method
# A class method is bound to the class & receives the class as an implicit first argument.

# Note - static method can't access or modify class state & generally for utility.

# staticmethod 

# There are many indirect ways to change the class attribute
class Person:
    name = "anonymous"

    # def changeName(self, name):
        # self.name = name
        # Person.name = name  # these is one method to change the class attribute
        # self.__class__.name  # 2nd method

    @classmethod   #decorator
    def changeName(cls, name):   # 3rd method by using classmethod
        cls.name = name

p1 = Person()
p1.changeName("Aman")
print(p1.name)
print(Person.name)
