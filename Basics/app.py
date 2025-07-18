"""This module demonstrates Python basics and object-oriented programming concepts."""

# ========================================
# Python Basics & Object-Oriented Concepts
# ========================================

# -----------------------------
# Variable Declarations & Types
# -----------------------------
NAME = "Alice"         # String
AGE = 25               # Integer
HEIGHT = 5.7           # Float
IS_STUDENT = True      # Boolean

# -----------------
# Commented Example
# -----------------
# Example for user input and printing
# print("Hello, World!")
# user_name = input("Enter your name: ")
# print("Hi", user_name)

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
unique_numbers = {1, 2, 3}
# print(unique_numbers)  # Output: {1, 2, 3}

# ----------------
# Looping in Python
# ----------------

# For loop
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)

# While loop
# count = 0
# while count < 5:
#     print(count)
#     count += 1

# ====================
# Object-Oriented Python
# ====================

# -----------------
# 1. Class and Object
# -----------------

# class Person:
#     """Represents a person with name and age."""
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         """Greet with name and age."""
#         print(f"Hi, I'm {self.name} and I'm {self.age} years old.")

# p1 = Person("Chetan", 23)
# p1.greet()

# ----------------
# 2. Inheritance & Data Hiding
# ----------------

# class BankAccount:
#     """A simple bank account class with deposit, withdraw, and balance check."""
#     def __init__(self, balance):
#         self.__balance = balance  # Private variable

#     def deposit(self, amount):
#         """Deposit the given amount."""
#         self.__balance += amount

#     def withdraw(self, amount):
#         """Withdraw the given amount if sufficient balance exists."""
#         if amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print("Insufficient funds")

#     def get_balance(self):
#         """Return the current balance."""
#         return self.__balance

# account = BankAccount(1000)
# account.deposit(500)
# account.withdraw(10000)
# print(f'Current balance: {account.get_balance()}')
# print(account.__balance)  # ❌ Error: Cannot access private attribute

# ----------------
# 3. Polymorphism
# ----------------

class Animal:
    """Base class representing an animal."""

    def speak(self):
        """Make a generic animal sound."""
        print("Some generic animal sound")


class Dog(Animal):
    """Dog class that overrides speak method."""

    def speak(self):
        """Make a dog sound."""
        print("Woof!")


class Cat(Animal):
    """Cat class that overrides speak method."""

    def speak(self):
        """Make a cat sound."""
        print("Meow!")


animals = [Dog(), Cat(), Animal()]
for animal in animals:
    animal.speak()

# ----------------
# 4. Encapsulation
# ----------------

class Car:
    """Represents a car with make and model."""

    def __init__(self, make, model):
        """Initialize the car with make and model."""
        self.__make = make
        self.__model = model

    def get_info(self):
        """Return make and model of the car."""
        return f"{self.__make} {self.__model}"

    def set_make(self, make):
        """Set a new make for the car."""
        self.__make = make

    def set_model(self, model):
        """Set a new model for the car."""
        self.__model = model


# Example usage
my_car = Car("Toyota", "Corolla")
print(my_car.get_info())  # Output: Toyota Corolla

# Uncomment to update details
# my_car.set_make("Honda")
# my_car.set_model("Civic")
# print(my_car.get_info())  # Output: Honda Civic
