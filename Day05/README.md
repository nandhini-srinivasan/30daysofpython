
# Day5 Functions: functions, parameters, return values, lambda functions

**Date:** june 2, 2025

🎯 **Challenge** - Write a function that computes the sum and average of a list of numbers

----

````markdown
# 🧠 Python Notes: Functions, Parameters, Return Values & Lambda

---

## 🧩 1. Functions

A **function** is a block of reusable code. It helps avoid repetition and keeps code organized.

```python
# ✅ Reuse the same code without writing again
# ✅ Makes code neat and modular
# ✅ Easy to debug and update
# ✅ Helps in teamwork and large projects
````

### 🔹 Syntax:

```python
def function_name():
    # code block
    pass
```

### 💡 Example:

```python
def greet():
    print("Hello, Nandhini!")  # This prints a welcome message

greet()  # calling the function
```

📤 **Output:**

```
Hello, Nandhini!
```

---

## 🧩 2. Function Parameters

Parameters are **inputs** to a function. They make functions flexible.

### ✅ Example:

```python
def greet(name):  # 'name' is a parameter
    print("Hello,", name)

greet("Nandhini")
greet("Rahul")
```

📤 **Output:**

```
Hello, Nandhini
Hello, Rahul
```

---

### 🔸 Different Types of Parameters

#### ✅ Default Parameter

```python
def greet(name="Friend"):
    print("Hello,", name)

greet()          # uses default
greet("Nandhini") # uses given value
```

📤 **Output:**

```
Hello, Friend
Hello, Nandhini
```

---

#### ✅ \*args → Multiple Positional Arguments

`*args` lets you pass any number of values. They’re collected into a **tuple**.

```python
def show_items(*items):  # Accepts any number of items
    for item in items:   # Loops through each item
        print(item)
        
show_items("apple", "banana", "cherry")
```

📤 **Output:**

```
apple
banana
cherry
```

### 💬 Why we use \*args?

* When we **don’t know** how many values will be passed
* To make our function **more flexible**

#### 💡 Example:

```python
def total_marks(*marks):
    return sum(marks)

print(total_marks(78, 85, 90))
```

📤 **Output:**

```
253
```

---

## 🧩 3. Return Values

We use `return` when we want the function to give back a **value**, not just print.

### ✅ Example:

```python
def add(a, b):
    return a + b  # returns the sum

result = add(3, 5)
print(result)
```

📤 **Output:**

```
8
```

---

## 🧩 4. Lambda Functions

Lambda = small anonymous (no-name) function. Use it for **one-line logic**.

### ✅ Example 1: Square of a number

```python
square = lambda x: x * x
print(square(4))
```

📤 **Output:**

```
16
```

### ✅ Example 2: Add two numbers

```python
add = lambda a, b: a + b
print(add(3, 5))
```

📤 **Output:**

```
8
```

---

## ✅ Final Checklist of Topics You’ve Learned

| Topic              | What You Learned                                         |
| ------------------ | -------------------------------------------------------- |
| Defining Functions | How to write and call a function using `def`             |
| Parameters         | How to pass input values to functions                    |
| Return Values      | How to use `return` to give back results from a function |
| Lambda Functions   | How to write short, one-line anonymous functions         |
| \*args             | How to pass multiple positional arguments flexibly       |
| Default Parameters | How to give default values to parameters                 |

---

## 🧠 Advanced – To Learn Later

| Topic            | Description                                       |
| ---------------- | ------------------------------------------------- |
| `**kwargs`       | Pass multiple named arguments (like dictionaries) |
| Nested Functions | A function inside another function                |
| Recursion        | When a function calls itself                      |
| Function Scope   | Local vs Global variables                         |
| Decorators       | Used in advanced Python and web frameworks        |

---

## 📌 Summary Example (Using All Concepts):

```python
def student_info(name, age=18, *skills):
    print("Name:", name)
    print("Age:", age)
    print("Skills:")
    for skill in skills:
        print("-", skill)

student_info("Nandhini", 22, "Python", "SQL", "Power BI")
```

📤 **Output:**

```
Name: Nandhini
Age: 22
Skills:
- Python
- SQL
- Power BI
```

### 🔍 How this works:

* `name` → gets `"Nandhini"`
* `age` → gets `22`
* `*skills` → gets the rest as a tuple: `("Python", "SQL", "Power BI")`

That’s how Python knows how to assign the values based on position! 🎯

---




