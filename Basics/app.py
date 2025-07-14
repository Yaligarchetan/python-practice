#python basics
#This is a simple Python script demonstrating variable declarations

name = "Alice"         # string
age = 25               # integer
height = 5.7           # float
is_student = True      # boolean

'''
print("Hello, World!")
user_name = input("Enter your name: ")
print("Hi", user_name)
'''

# Data Types in Python
'''
# List
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # apple

# Tuple (immutable)
colors = ("red", "green", "blue")

# Dictionary (key-value pairs)
person = {"name": "Bob", "age": 30}
print(person["name"])  # Bob

# Set (unique items)
unique_numbers = {1, 2, 3, 3, 2}
print(unique_numbers)  # {1, 2, 3}
'''
# looping in python
'''
# For loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

    

# While loop
count = 0
while count < 5:
    print(count)
    count += 1
'''
#OOPS in Python
 # 1. Class and Object
'''
class Person:
    def __init__(self, name, age):  # constructor
        self.name = name            # instance variable
        self.age = age

    def greet(self):                # method
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")

# Creating an object
p1 = Person("chetan", 23)
p1.greet()
'''

# 2. Inheritance
#Use _ (protected) and __ (private) to hide data.
'''
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private variable

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
print(f'current balance: {account.get_balance()}')  # ✅ OK
#print(account.__balance)  # ❌ Error: __balance is private and cannot be accessed directly
'''



