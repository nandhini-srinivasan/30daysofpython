

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
* Final password → "Nand$7F@"

### 💻 Code Example:

```python
import random  # To generate random values
import string  # To get letters, digits, and symbols

# Define a function to suggest a strong password based on email
def suggest_password(email):
    username = email.split('@')[0]  # Take the part before '@' in the email
    base = username[:4].capitalize()  # Take first 4 letters and capitalize the first letter

    # Combine digits, symbols, and uppercase letters to make the password strong
    extras = string.digits + string.punctuation + string.ascii_uppercase

    # Pick 4 random characters from extras and join them into a string
    random_part = ''.join(random.choice(extras) for _ in range(4))

    # Combine base + random part to make final password
    password = base + random_part

    return password  # Return the final password

# Use the function with an example email
email = "nandhini123@gmail.com"
print("Suggested Password:", suggest_password(email))  # Print the generated password


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


## Concepts Used

| Concept                  | Description                                                 |
| ------------------------ | ----------------------------------------------------------- |
| `email.split('@')[0]`    | Gets the username part before `@`                           |
| `[:4].capitalize()`      | Takes the first 4 letters and makes the first one uppercase |
| `string.digits`          | All numbers from 0–9                                        |
| `string.punctuation`     | Special characters like `@`, `#`, `$`, etc.                 |
| `string.ascii_uppercase` | All capital letters from A–Z                                |
| `random.choice()`        | Picks one random item from a list                           |
| `''.join(...)`           | Combines items into one string                              |

---

## ✅ Summary

* Modules help organize and reuse your code.
* Python has built-in modules like `math` and `random`.
* You can create your own custom module.
* You built a practical tool: a strong, personalized password generator.

---



---



# commonly used built-in Python modules

To help simplify tasks like file handling, math operations, time management, data parsing, and more.

These modules come pre-installed with Python.

---

## 📦 Top Modules to Know

| Module        | Purpose                                | Example Use Case                              |
| ------------- | -------------------------------------- | --------------------------------------------- |
| `math`        | Mathematical functions                 | Square root, rounding, trigonometry           |
| `random`      | Generate random values                 | Games, OTP/password creation, simulations     |
| `string`      | Useful string constants                | Letters, digits, punctuation for validation   |
| `datetime`    | Work with dates and times              | Timestamps, age calculator, countdowns        |
| `time`        | Control program timing                 | Delays, performance tracking                  |
| `os`          | Interact with the operating system     | File paths, folder creation, environment vars |
| `sys`         | System-specific functionality          | Command-line args, script exits               |
| `csv`         | Read and write CSV files               | Data analysis, file parsing                   |
| `json`        | Handle JSON data                       | APIs, config files                            |
| `statistics`  | Basic statistical operations           | Mean, median, mode, standard deviation        |
| `re`          | Regular expressions (pattern matching) | Email validation, search & replace            |
| `collections` | Enhanced data structures               | Counters, default dictionaries, namedtuples   |

---

## 🧪 Code Snippets (Examples)

### ✅ `math`

```python
import math
print(math.sqrt(25))  # Output: 5.0
```

### ✅ `random`

```python
import random
print(random.randint(1, 10))  # Random number between 1 and 10
```

### ✅ `string`

```python
import string
print(string.ascii_letters)  # abc...XYZ
```

### ✅ `datetime`

```python
from datetime import datetime
print(datetime.now())  # Current date and time
```

### ✅ `os`

```python
import os
print(os.getcwd())  # Current directory
```

### ✅ `csv`

```python
import csv
with open('file.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

### ✅ `json`

```python
import json
data = '{"name": "Nandhini", "age": 22}'
parsed = json.loads(data)
print(parsed["name"])  # Output: Nandhini
```

### ✅ `statistics`

```python
import statistics
print(statistics.mean([10, 20, 30]))  # Output: 20
```

### ✅ `re`

```python
import re
email = "nandhini123@gmail.com"
if re.match(r"\w+@\w+\.\w+", email):
    print("Valid email!")
```

---


