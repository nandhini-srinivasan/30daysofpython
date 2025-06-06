

### ➤ Create a Car class with attributes and a display method

```python
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display(self):
        print(f"Car Info: {self.year} {self.brand} {self.model}")
```

### ✅ Using the Car class:

```python
car1 = Car("Toyota", "Innova", 2020)
car2 = Car("Tata", "Punch", 2024)

car1.display()  # Car Info: 2020 Toyota Innova
car2.display()  # Car Info: 2024 Tata Punch
```

---
