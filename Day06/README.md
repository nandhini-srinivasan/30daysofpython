

---


# Day 06️⃣: Modules and Packages  
📅 **Date**: June 2, 2025  

## 🗒️ Topics Covered
- Importing built-in modules (`math`, `random`)
- Creating a custom module
- 💡 Challenge: Generate a random 8-character password

---

## 🔹 1. What Are Modules and Packages?

### 📦 Module
A **module** is a `.py` file that contains Python code like functions, variables, or classes.

✅ **Purpose**: Helps you reuse code instead of writing it again and again.

#### Example:

**`greetings.py`**
```python
def say_hello():
    print("Hello, Nandhini!")
````

**Usage in another file:**

```python
import greetings

greetings.say_hello()  # Output: Hello, Nandhini!
```

---

### 📁 Package

A **package** is a **folder** that contains multiple `.py` files (modules) along with an `__init__.py` file.

✅ Think of it as a **folder of useful tools**.

> For now, focus on **modules**. Packages become important in larger projects.

---

## 🔹 2. Using Built-in Modules

### 🧮 `math` Module

Useful for mathematical operations.

```python
import math

print(math.sqrt(25))      # Square root → 5.0
print(math.ceil(4.3))     # Round up → 5
print(math.floor(4.9))    # Round down → 4
```

---

### 🎲 `random` Module

Used for generating random numbers or picking random values.

```python
import random

print(random.randint(1, 10))                 # Random number between 1 and 10
print(random.choice(['a', 'b']))             # Randomly picks 'a' or 'b'
```

---

## 🔹 3. Creating Your Own Module

### ✅ Steps:

1. Create a Python file with reusable functions (e.g., `mytools.py`)
2. Import and use it in other Python files

#### Example:

**`mytools.py`**

```python
def greet(name):
    print(f"Hi {name}, you're doing great!")
```

**`main.py`**

```python
import mytools

mytools.greet("Nandhini")  # Output: Hi Nandhini, you're doing great!
```

---

## 🔹 4. 🎯 Challenge: Generate a Random 8-Character Password

### ✅ Goal:

Create a strong, memorable password using:

* Part of the email
* Random symbols, digits, and uppercase letters

### 💡 Concept:

For the email `nandhini123@gmail.com`:

* Extract part before `@` → `"nandhini123"`
* Use first 4 characters → `"nand"` → Capitalize → `"Nand"`
* Add 4 random characters (digits + punctuation + uppercase letters)

### 💻 Code Example:

```python
import random
import string

def suggest_password(email):
    username = email.split('@')[0]            # 'nandhini123'
    base = username[:4].capitalize()          # 'Nand'
    
    extras = string.digits + string.punctuation + string.ascii_uppercase
    random_part = ''.join(random.choice(extras) for _ in range(4))
    
    password = base + random_part
    return password

# Test
email = "nandhini123@gmail.com"
print("Suggested Password:", suggest_password(email))
```

### 📝 Sample Output:

```
Suggested Password: Nand$7G@
```

### ✅ Why It's Good:

* 🔐 **Strong**: includes symbols, numbers, uppercase
* 🧠 **Memorable**: uses your name/email
* 🛠️ **Customizable**: you can change length, characters, etc.

---

## ✅ Summary

* Modules help organize and reuse your code.
* Python has built-in modules like `math` and `random`.
* You can create your own custom module.
* You built a practical tool: a strong, personalized password generator.

---

