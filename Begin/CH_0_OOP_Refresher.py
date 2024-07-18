# Introduction to Object-Oriented Programming with Python: Creating and Using Classes

# Class Definition
class Car:
   # Constructor (Initialization) - __init__ method
   def __init__(self, make, model):
   #self refers to the car that is created
   # Encapsulation: Attributes (make and model) are encapsulated within the class.
   #Encapsulation heights the internal details of an object and 
   # exposes only what is necessary. Think of it as specifying the unique characteristic 
   # of each car. Self.make equals make, self.model equals model. 
   
       self.make = make
       self.model = model

   # Method - start_engine
   def start_engine(self):
       # Encapsulation: Accessing attributes through self.
       print(f"The {self.make} {self.model}'s engine is running!")


# Creating instances (objects) of the Car class

# Inheritance: Car is a class that can be used to create objects (instances).
# Abstraction: We create objects without worrying about the internal details of the Car class.

# Creating the first car (object)
car1 = Car("Toyota", "Camry")

# Creating the second car (object)
car2 = Car("Ford", "Mustang")


# Accessing object attributes
print(f"I have a {car1.make} {car1.model}")
print(f"I also own a {car2.make} {car2.model}.")
# Encapsulation: Accessing object attributes (make and model) using dot notation.


# Calling object methods

# Polymorphism: Different objects (car1 and car2) can perform the same action (start_engine).
# Method OVerriding: The start_engine method may be customised in subclasses.
# Method Call - start_engine
car1.start_engine()
car2.start_engine()