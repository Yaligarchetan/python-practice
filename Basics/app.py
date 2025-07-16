# ========================================
# Python Basics & Object-Oriented Concepts
# ========================================

# -----------------------------
# Variable Declarations & Types
# -----------------------------
name = "Alice"         # String
age = 25               # Integer
height = 5.7           # Float
is_student = True      # Boolean

# -----------------
# Commented Example
# -----------------
'''
print("Hello, World!")
user_name = input("Enter your name: ")
print("Hi", user_name)
'''

# ------------------------
# Built-in Data Structures
# ------------------------

# List
fruits = ["apple", "banana", "cherry"]
# print(fruits[0])  # Output: apple

# Tuple (immutable)
colors = ("red", "green", "blue")

# Dictionary (key-value pairs)
person = {"name": "Bob", "age": 30}
# print(person["name"])  # Output: Bob

# Set (unique items)
unique_numbers = {1, 2, 3, 3, 2}
# print(unique_numbers)  # Output: {1, 2, 3}

# ---------------
# Looping in Python
# ---------------

# For loop
'''
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
'''

# While loop
'''
count = 0
while count < 5:
    print(count)
    count += 1
'''

# ====================
# Object-Oriented Python
# ====================

# -----------------
# 1. Class and Object
# -----------------
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")

p1 = Person("Chetan", 23)
p1.greet()
'''

# ----------------
# 2. Inheritance & Data Hiding
# ----------------
'''
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
account.withdraw(10000)
print(f'Current balance: {account.get_balance()}')
# print(account.__balance)  # ❌ Error: Cannot access private attribute
'''

# ----------------
# 3. Polymorphism
# ----------------

class Animal:
    def speak(self):
        print("Some generic animal sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

animals = [Dog(), Cat(), Animal()]
for animal in animals:
    animal.speak()

# ----------------
# 4. Encapsulation
# ----------------

class Car:
    def __init__(self, make, model):
        self.__make = make    # Private attribute
        self.__model = model  # Private attribute

    def get_info(self):
        return f"{self.__make} {self.__model}"

    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

# Example usage
my_car = Car("Toyota", "Corolla")
print(my_car.get_info())  # Output: Toyota Corolla

# Uncomment to update details
# my_car.set_make("Honda")
# my_car.set_model("Civic")
# print(my_car.get_info())  # Output: Honda Civic
