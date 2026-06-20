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



# 3. Student
# Create a Student class with:

# __init__ that receives name (str), _grades (empty list by default)
# add_grade(grade) that adds a grade (validate: 0 <= grade <= 10)
# @property average that returns grade average (or 0 if list is empty)
# @property status that returns "Approved" if average >= 7, otherwise "Reprobbed"
# @classmethod top_students(all_students) that returns a list of students with average >= 8
# __repr__ that returns Student('John', 7.5) (without quotes around name)

# import statistics

# class Student:
#     students = []

#     def __init__(self, name: str):
#         self.name = name
#         self._grades = []
#         Student.students.append(self)

#     def add_grade(self, grade: int):
#         if not(0 <= grade <= 10):
#             raise ValueError(f'Grade must be between 0 and 10.')
#         self._grades.append(grade)

#     @property
#     def average(self):
#         return statistics.mean(self._grades) if self._grades else 0

#     @property
#     def status(self):
#         return 'Approved' if self.average >= 7 else 'Reprobbed'

#     @classmethod
#     def top_students(cls, all_students):
#         return [student for student in all_students if student.average >= 8]

#     def __repr__(self):
#         return f"Student('{self.name}', {self.average})"


# # Uso:
# mario = Student('Mario')
# mario.add_grade(8)
# mario.add_grade(9)

# chunda = Student('Chunda')
# chunda.add_grade(6)

# print(mario)  # Student('Mario', 8.5)
# print(mario.status)  # Approved

# print(Student.top_students(Student.students))  # [Student('Mario', 8.5)]




# 4. Movie
# Create a Movie class with:

# __init__ that receives title (str), _year (int), _rating (float)
# Validation in __init__: rating must be between 0 and 10, otherwise raise ValueError
# @property is_classic that returns True if year <= 1980
# @property is_highly_rated that returns True if rating >= 7.5
# update_rating(new_rating) that updates with validation
# A class list movies that stores all instances
# @classmethod by_year(year) that returns all movies from a specific year
# __str__ that returns "The Matrix (1999) - Rating: 8.7/10"

# class Movie:
#     movies = []

#     def __init__(self, title: str, year: int, rating: float):
#         if not(0 <= rating <= 10):
#             raise ValueError(f'Rating must be between 0 and 10.')
#         self.title = title
#         self._year = year
#         self._rating = rating
#         Movie.movies.append(self)

#     def __str__(self):
#         return f'{self.title} ({self._year}) - Rating: {self._rating}/10'

#     @property
#     def is_classic(self):
#         return self._year <= 1980
    
#     @property
#     def is_highly_rated(self):
#         return self._rating >= 7.5
    
#     def update_rating(self, new_rating: float):
#         if not(0 <= new_rating <= 10):
#             raise ValueError(f'Rating must be between 0 and 10.')
#         self._rating = new_rating
    
#     @classmethod
#     def by_year(cls, year):
#         movies = [movie for movie in cls.movies if movie._year == year]
#         for movie in movies:
#             print(movie)
#         return movies # feito com list comprehension, mas do jeito mais simplificado poderia ser assim:
#         # year_list = []
#         # for movie in Movie.movies:
#         #     if movie._year == year:
#         #         year_list.append(movie)  # Só adiciona o filme mesmo
#         # return year_list


# # Uso:
# movie1 = Movie('The Matrix', 1999, 8.7)
# movie2 = Movie('Jaws', 1975, 8.0)
# movie3 = Movie('Inception', 2010, 8.8)

# print(movie1)  # The Matrix (1999) - Rating: 8.7/10
# print(movie1.is_classic)  # False
# print(movie2.is_classic)  # True
# Movie.by_year(1975)



# 5. Employee
# Create an Employee class with:

# __init__ that receives name (str), _salary (float), _department (str)
# @property formatted_salary that returns salary formatted as "$5000.00"
# give_raise(percentage) that increases salary (validate: percentage > 0)
# change_department(new_department) with validation (department cannot be empty/None)
# A class variable employees (list) that stores all instances
# @classmethod employees_by_department(department) that returns list of employees in a department
# @classmethod average_salary_by_department(department) that calculates average salary for a department
# __str__ that returns "John (IT) - $5000.00"
# __eq__ that compares two employees by name

class Employee:

    employees = []

    def __init__(self, name: str, salary: float, department: str):
        self.name = name
        self._salary = salary
        self._department = department
        Employee.employees.append(self)

    def __str__(self):
        return f'{self.name} ({self._department} - {self._salary})'
    
    @property
    def fromatted_salary(self):
        return f'${self._salary:,.2f}'


        
    





        