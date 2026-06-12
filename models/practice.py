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

class Restaurant:

    restaurants = []

    def __init__(self, name: str, category: str, active:False, capacity: int, evaluation: int):
        if not(1 <= evaluation <= 10):
            raise ValueError(f'Evaluation must be between 1 and 10.') # error handling on the evaluation grade
        
        self.name = name
        self.category = category
        self.active = active
        self.capacity = capacity
        self.evaluation = evaluation
        Restaurant.restaurants.append(self)

    @staticmethod
    def show_restaurants():
        for restaurant in Restaurant.restaurants:
            print(f'- Restaurant {restaurant.name} | Category: {restaurant.category} | Is Active: {'Not Active' if restaurant.active == False else 'Active'} | User evaluation: {restaurant.evaluation}')
    

# Seed data
Restaurant("La Trattoria", "Italiana", False, 50, 9)
Restaurant("Burger Town", "Fast Food", True, 30, 7)
Restaurant("Sushi Zen", "Japonesa", True, 40, 10)
Restaurant("Taco Loco", "Mexicana", False, 25, 6)
Restaurant("Le Petit Bistro", "Francesa", True, 20, 8)
Restaurant("Curry House", "Indiana", True, 35, 9)
Restaurant("Vegan Delight", "Vegana", False, 15, 8)
Restaurant("Steak House", "Churrascaria", True, 60, 9)
Restaurant("Pizza Palace", "Italiana", True, 45, 7)
Restaurant("Dim Sum Express", "Chinesa", False, 50, 8)

Restaurant.show_restaurants()
        