# Inheritance
# When one class (child/derived) derives the properties & methods of another class(parent/base)

class Car:

    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("Car stopped")

class ToyatoCar(Car):
    def __init__(self, name):
        self.name = name

car1 = ToyatoCar("Fortuner")
car2 = ToyatoCar("Prius")
print(car1.name)
car1.start()
car1.stop()
print()


# Types Of Inheritance
# 1. Single Inheritance
# Single base class and single child class

# Multi-level Inheritance
# One base class --> Child class  --> child class -->
class Car:
    @staticmethod
    def start():
        print("Car started..")
    @staticmethod
    def stop():
        print("Car stopped")

class ToyatoCar(Car):
    def __init__(self, brand):
        self.brand = brand

class Fortuner(ToyatoCar):
    def __init__(self,brand, type):
        # super() calls the constructor of ToyatoCar
        super().__init__(brand)
        self.type = type

car1 = Fortuner("Fortuner","diesel")
print(car1.type)
car1.start()
print(car1.brand)
print()

# Multiple Inheritance
# When we inherit the properties of more that 2 base class in one child class it is konwn as Muitiple

class Camera:
    def take_photo(self):
        print("Click! Photo saved to gallery.")

class Phone:
    def make_call(self, number):
        print(f"Calling {number}...")

# Multiple Inheritance: SmartPhone inherits from BOTH
class SmartPhone(Camera, Phone):
    def __init__(self, model):
        self.model = model
    
    def check_email(self):
        print("Checking inbox...")

# Using the object
my_phone = SmartPhone("iPhone 15")

my_phone.make_call("9876543210") # From Phone class
my_phone.take_photo()            # From Camera class
my_phone.check_email()           # From its own class

