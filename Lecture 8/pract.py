class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks= marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi", self.name,"your avg score is ",  sum/3)
    
# s1 = Student("Roonya", [90, 80, 68])
# s1.get_avg()

# s1.name = 'ironman'
# s1.get_avg()


class Account:

    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance

    # credit method
    def credit(self, amount):
        self.balance += amount
        print("Rs", amount, "was credited to your account")
        print("total balance", self.get_balance())

    # debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs", amount, "was debited from your account")
        print("Total balance", self.get_balance())

    def get_balance(self):
        return self.balance


acc1 = Account(12345, 1000)
print(acc1.balance)
acc1.debit(100)
acc1.credit(50)


