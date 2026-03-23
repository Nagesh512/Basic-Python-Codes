# Polymorphism
# poly - many    morph -- forms

# When the same operator is allowed to have different meaning according to context

print(1 + 2)  #3
print(type(1))

print("Apna" + "college")  # concatenate
print(type("Apna"))

print([1, 2, 3] + [4, 5, 6]) # merge
print(type([1, 2, 3]))

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def show(self):
        print(self.real, "i + ", self.imag, "j")

    # def add(self, num2):
    def __add__(self, num2):   #dunder
        newReal = self.real + num2.real
        newImag = self.imag + num2.imag
        return Complex(newReal,newImag)
    
    def __sub__(self, num2):   #dunder
        newReal = self.real - num2.real
        newImag = self.imag - num2.imag
        return Complex(newReal,newImag)

num1 = Complex(1, 4)
num1.show()

num2 = Complex(4, 6)
num2.show()

# num3 = num1.add(num2)
num3 = num1 + num2
num4 = num1 - num2
num3.show()
num4.show()
