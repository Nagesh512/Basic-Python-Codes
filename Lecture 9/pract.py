class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return (2 * 3.14 * self.radius)
    
c1 = Circle(8)
print(c1.area())
print(c1.perimeter())


class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.dept = department
        self.sal = salary
    
    def showdetails(self):
        print("role = ", self.role)
        print("department = ", self.dept)
        print("salary = ", self.sal)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("data engineer", "EDW-3", "1,00,000")

# e1 = Employee("data Engineer", "EDW-3", 50000)
# e1.showdetails()

engg1 = Engineer("Elon", 26)
engg1.showdetails()


class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, ord2):   # dunder function for greater than
        return self.price > ord2.price
    
    
ord1 = Order("chips", 20)
ord2 = Order("tea", 15)

print(ord1 > ord2)