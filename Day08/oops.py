

# 🎯 Challenge Task - Day 08: Object-Oriented Programming (Part 1)
# Create a Car class with attributes and a display method

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display(self):
        print(f"Car Info: {self.year} {self.brand} {self.model}")


# Creating objects of the Car class
car1 = Car("Toyota", "Innova", 2020)
car2 = Car("Tata", "Punch", 2024)

# Calling the display method
car1.display()   # Output: Car Info: 2020 Toyota Innova
car2.display()   # Output: Car Info: 2024 Tata Punch
