 **Day 08 - Object-Oriented Programming (Part 1)** 

---

````markdown
# 🚀 Day 0️⃣8️⃣: Object-Oriented Programming (Part 1)

📅 Date: June 6, 2025

---

## 🧠 Topics Covered

- What is OOP?
- Classes & Objects
- The `__init__()` Constructor
- Attributes (Class & Instance)
- Methods
- Challenge Task

---

## 🔹 What is Object-Oriented Programming?

OOP (Object-Oriented Programming) is a style of programming that helps structure code using **classes** and **objects**, mimicking real-world entities.

---

## 🔹 1. Class and Object

### ✅ Class
A blueprint to create objects. It contains methods (functions) and attributes (variables).

### ✅ Object
An actual instance created from the class.

```python
class Dog:
    # Class attribute
    species = "Canis familiaris"

    # Constructor
    def __init__(self, name, age):
        self.name = name      # Instance attribute
        self.age = age

    # Method
    def bark(self):
        return f"{self.name} says Woof!"
````

### Creating Objects and Using Methods:

```python
dog1 = Dog("Tommy", 3)
dog2 = Dog("Rocky", 5)

print(dog1.name)         # Tommy
print(dog2.age)          # 5
print(dog1.bark())       # Tommy says Woof!
```

---

## 🔹 2. The `__init__()` Method

The constructor method runs automatically when an object is created.

```python
def __init__(self, param1, param2):
    self.param1 = param1
    self.param2 = param2
```

---

## 🔹 3. Attributes

### ✅ Class Attribute

Shared by all instances of the class.

### ✅ Instance Attribute

Unique for each object.

```python
class Student:
    college = "XYZ College"  # Class attribute

    def __init__(self, name, roll):
        self.name = name      # Instance attributes
        self.roll = roll

s1 = Student("Nandhini", 101)
s2 = Student("Ravi", 102)

print(s1.college)   # XYZ College
print(s1.name)      # Nandhini
print(s2.name)      # Ravi
```

---

## 🔹 4. Methods

Functions defined inside a class that usually operate on its attributes.

```python
class Calculator:
    def add(self, a, b):
        return a + b

calc = Calculator()
print(calc.add(5, 3))  # Output: 8
```

---

## 🧾 Summary Table

| Concept     | Purpose                        | Syntax Example               |
| ----------- | ------------------------------ | ---------------------------- |
| Class       | Blueprint for creating objects | `class MyClass:`             |
| Object      | Instance of a class            | `obj = MyClass()`            |
| Constructor | Initialize object state        | `def __init__(...)`          |
| Attributes  | Store object data              | `self.name = name`           |
| Methods     | Define object behaviors        | `def display(self): ...`     |
| `self`      | Refers to the object itself    | Used in all instance methods |

---



## 🧠 Learning Note


Let’s keep going 🚀
Next up → Part 2: Inheritance, Encapsulation, Polymorphism!




