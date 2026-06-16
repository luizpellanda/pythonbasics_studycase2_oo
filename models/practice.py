# Basic Object-Oriented Vehicle Model
# A foundational exercise in Object-Oriented Programming (OOP) to understand class instantiation and attribute assignment.

# Inputs: None (parameters defined within the class constructor).

# Logic: * Define a class car with initialization attributes: model, color, and year.

# Implement an instantiation process to create a concrete object.

# Assign specific values to the object's attributes.

# Outputs: A verification of the object's state (printing the attributes to the console).

# cars = []

# class Car:    

#     def __init__(self, model: str, color: str, year=0):
#         self.model = model
#         self.color = color
#         self.year = year
#         cars.append(self)

#     def show_cars():
#         for car in cars:
#             print(f'- {car.model} | {car.color} | {car.year}')

# car_fusca = Car('Fusca', 'Red', 1978)
# car_gol = Car('Gol', 'Blue', 1954)

# Car.show_cars()





# Restaurant Object Modeling
# A practical exercise in Object-Oriented Programming (OOP) focused on defining entities and managing their state through class attributes.

# Inputs: Parameters defined within the class constructor (__init__).

# Logic:

# Define a class Restaurante with mandatory attributes: name, category, and active (boolean).

# Extend the class with two additional relevant attributes (e.g., capacity and evaluation).

# Perform instantiation and attribute assignment.

# Outputs: A visualization of the created object's state, demonstrating the encapsulation of restaurant data.

# class Restaurant:

#     restaurants = []

#     def __init__(self, name: str, category: str, active:False, capacity: int, evaluation: int):
#         if not(1 <= evaluation <= 10):
#             raise ValueError(f'Evaluation must be between 1 and 10.') # error handling on the evaluation grade
        
#         self.name = name
#         self.category = category
#         self.active = active
#         self.capacity = capacity
#         self.evaluation = evaluation
#         Restaurant.restaurants.append(self)

#     @staticmethod
#     def show_restaurants():
#         for restaurant in Restaurant.restaurants:
#             print(f'- Restaurant {restaurant.name} | Category: {restaurant.category} | Is Active: {'Not Active' if restaurant.active == False else 'Active'} | User evaluation: {restaurant.evaluation}')
    
# # Seed data
# Restaurant("La Trattoria", "Italiana", False, 50, 9)
# Restaurant("Burger Town", "Fast Food", True, 30, 7)
# Restaurant("Sushi Zen", "Japonesa", True, 40, 10)
# Restaurant("Taco Loco", "Mexicana", False, 25, 6)
# Restaurant("Le Petit Bistro", "Francesa", True, 20, 8)
# Restaurant("Curry House", "Indiana", True, 35, 9)
# Restaurant("Vegan Delight", "Vegana", False, 15, 8)
# Restaurant("Steak House", "Churrascaria", True, 60, 9)
# Restaurant("Pizza Palace", "Italiana", True, 45, 7)
# Restaurant("Dim Sum Express", "Chinesa", False, 50, 8)

# Restaurant.show_restaurants()




# Exercise 1: Product with @property
# Create a Product class with:

# Attributes: name, price, quantity (private with _)
# __str__ method that returns something like: "MacBook Pro | $1999"
# A @property called total_value that returns price * quantity
# A @property called in_stock that returns "✅ In Stock" if quantity > 0, otherwise "❌ Out of Stock"
# A class method list_products() that lists all created products

# Create 3 products and list them.

# class Product:
#     products = []

#     def __init__(self, name, price, quantity):
#         self.name = name
#         self._price = price
#         self._quantity = quantity
#         Product.products.append(self)
    
#     def __str__(self):
#         return f"{self.name} | ${self._price}"
    
#     @property
#     def total_value(self):
#         return self._price * self._quantity
    
#     @property
#     def in_stock(self):
#         return '✅ In Stock' if self._quantity > 0 else '❌ Out of Stock'
    
#     @classmethod
#     def show_products(cls):
#         print(f"{'Product:'.ljust(25)} | {'Price:'.ljust(10)} | {'Quantity:'.ljust(10)} | {'Total Value:'.ljust(15)} | {'Status:'.ljust(15)}")
#         for product in cls.products:
#             print(f"{product.name.ljust(25)} | ${str(product._price).ljust(9)} | {str(product._quantity).ljust(10)} | ${str(product.total_value).ljust(14)} | {product.in_stock.ljust(15)}")

# Product("MacBook Pro 16", 2499, 5)
# Product("iPhone 15 Pro", 999, 12)
# Product("Sony WH-1000XM5", 399, 8)
# Product("iPad Air", 599, 3)
# Product("Apple Watch Ultra", 799, 0)
# Product("AirPods Pro", 249, 15)
# Product("Magic Keyboard", 349, 2)
# Product("USB-C Hub", 79, 20)
# Product("Monitor LG 4K", 499, 1)
# Product("Webcam Logitech", 129, 0)

# Product.show_products()




# Exercise 2: Bank Account with @property and setter
# Create a BankAccount class with:

# Attributes: account_number, owner, _balance (private)
# __str__ returning: "Account 12345 | Owner: John | Balance: $1500"
# @property balance that returns the balance formatted as currency
# @balance.setter that only allows setting balance if it's positive (otherwise print error)
# Method withdraw(amount) that removes money
# Method deposit(amount) that adds money
# A class list accounts that stores all accounts

# Create 2 accounts, do operations, list them.

# class BankAccount:

#     accounts = []

#     def __init__(self, account_number: int, owner: str, balance: float):
#         self.account_number = account_number
#         self.owner = owner
#         self._balance = balance
#         BankAccount.accounts.append(self)

#     def __str__(self):
#         return f"Account: {self.account_number} | Owner: {self.owner} | Balance: ${self._balance:,.2f}"
    
#     @property
#     def balance(self):
#         return f"${self._balance:,.2f}"
    
#     @balance.setter
#     def balance(self, amount: float):
#         if amount >= 0:
#             self._balance = amount
#         else:
#             print("❌ Balance cannot be negative!")
    
#     def withdraw(self, amount: float):
#         if amount > self._balance:
#             print(f"❌ Insufficient funds! Available: ${self._balance:,.2f}")
#         elif amount <= 0:
#             print("❌ Amount must be positive!")
#         else:
#             self._balance -= amount
#             print(f"✅ Withdrew ${amount:,.2f}. New balance: ${self._balance:,.2f}")
    
#     def deposit(self, amount: float):
#         if amount <= 0:
#             print("❌ Amount must be positive!")
#         else:
#             self._balance += amount
#             print(f"✅ Deposited ${amount:,.2f}. New balance: ${self._balance:,.2f}")

#     @classmethod
#     def show_accounts(cls):
#         print(f"\n{'Account Number'.ljust(20)} | {'Owner'.ljust(15)} | {'Balance'.ljust(15)}\n")
#         for account in cls.accounts:
#             print(f"{str(account.account_number).ljust(20)} | {account.owner.ljust(15)} | {account.balance.ljust(15)}")


# # Seed Data
# BankAccount(45668, 'Luiz', 9877)
# BankAccount(12345, 'Maria', 5000)

# BankAccount.show_accounts()

# # Operações
# BankAccount.accounts[0].withdraw(500)
# BankAccount.accounts[0].deposit(200)
# BankAccount.accounts[1].withdraw(1000)

# BankAccount.show_accounts()