# Program 1: Simple Class and Object
class MyClass:
    x = 5

p1 = MyClass()
print("Value of x in MyClass:", p1.x)
print()

# Program2: 
class Employee:
    company = "ABC Ltd"

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)
        print("Company:", Employee.company)

e1 = Employee("Rahul")
e2 = Employee("Riya")
e1.display()
e2.display()

# Program3: Student Class to Calculate Average Marks
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        total = 0
        for val in self.marks:
            total += val
        print("Hi", self.name, "your average score is:", total / len(self.marks))

s1 = Student("Riya", [86, 86, 90])
s1.get_avg()

s1.name = "Ironman"
s1.get_avg()

# Program 4: Bank Account using Class and Object
class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("Amount left:", self.balance)

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("Amount left:", self.balance)

acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(2000)


# Program 5: Animal Class with Cat and Dog subclasses (Inheritance)
class Animal:
    def __init__(self, name, shape):
        self.name = name
        self.shape = shape

    def show_details(self):
        print("Name:", self.name)
        print("Shape:", self.shape)
        print()

class Cat(Animal):
    def __init__(self, name, shape, features):
        super().__init__(name, shape)
        self.features = features

    def show_cat(self):
        self.show_details()
        print("Features:", self.features)
        print()

class Dog(Animal):
    def __init__(self, name, shape, features, breeds):
        super().__init__(name, shape)
        self.features = features
        self.breeds = breeds

    def show_dog(self):
        self.show_details()
        print("Features:", self.features)
        print("Breed:", self.breeds)
        print()

d1 = Dog("Oreo", "round", "bark", "pug")
c1 = Cat("Abc", "triangle", "claws")

d1.show_dog()
c1.show_cat()
