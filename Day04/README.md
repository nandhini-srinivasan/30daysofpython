# Day4 Control Structures: if-else, Loops, break & continue

**Date:** May 31, 2025

🎯 **Challenge** - Check if a user-entered number is prime

---

## 🧠 What are Control Structures?

Control structures are blocks that decide the **flow of a program** — they help us make decisions and repeat actions.

---

## 1. 🧪 If-Else Statements

Used to **make decisions** based on conditions.

### 🔹 Basic Syntax:

```python
if condition:
    # code runs if condition is True
elif another_condition:
    # code runs if this condition is True
else:
    # code runs if no condition is True
```

### 🔸 Example: Check if Number is Even or Odd

```python
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("number is even")
else:
    print("number is odd")
```

### ✅ Example 1: Voting Eligibility

```python
age = 18
if age >= 18:
    print("You are eligible to vote!")
else:
    print("You are not eligible to vote.")
```

### ✅ Example 2: Grading System

```python
marks = 75
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")
```

---

## 2. 🔁 Loops in Python

Loops help us **repeat a block of code**.

### 🔸 For Loop

Used to iterate over a **sequence** (like list, string, etc.)

#### ✅ Example 1: Loop Through a List

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

#### ✅ Example 2: Using range()

```python
for i in range(1, 6):
    print(i)
```

### 🔸 While Loop

Repeats as long as a condition is `True`

#### ✅ Example:

```python
count = 1
while count <= 5:
    print("Count is:", count)
    count += 1
```

### 🔸 else with Loops

The `else` block runs **only if loop ends without break**. Good for **prime number checks**!

#### ✅ Prime Check Example:

```python
for i in range(2, 5):
    if 10 % i == 0:
        print("Not a prime")
        break
else:
    print("Prime number")
```

---

## 🔂 Nested Loops

Loop **inside another loop**.

* Useful for **grids**, **tables**, and **patterns**

### ✅ Example: Print a 3x3 Grid

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
```

---

## ⚠️ Infinite Loop

Use `while True` when you want a loop to run **forever** (until `break` is used).

```python
while True:
    print("This runs forever unless you break it.")
```

---

## 3. ⛔ break and continue

### 🔸 `break`: Exit the loop immediately

### 🔸 `continue`: Skip current iteration and go to next

### ✅ Example 1: Using break

```python
for i in range(1, 10):
    if i == 5:
        break
    print(i)
```

#### 🍬 Candy Stock Example:

```python
av = 5
x = int(input("How many candies you want? "))
i = 1
while i <= x:
    if i > av:
        print("Out of stock")
        break
    print("Candy")
    i += 1
print("Bye")
```

### ✅ Example 2: Using continue

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

#### ✅ Example: Skip Multiples of 3

```python
for i in range(1, 101):
    if i % 3 == 0:
        continue
    print(i)
print("bye")
```

---

## 🧱 Note: Indentation is Important!

Python uses **indentation (spaces)** to define blocks. Wrong indent = Error!

```python
if True:
    print("Correct")  # ✅ Properly indented
  # print("Wrong")    # ❌ Will cause an error
```

---

## 📌 Summary Table

| Concept    | What it Does             |
| ---------- | ------------------------ |
| if-else    | Makes decisions          |
| for loop   | Loops through sequences  |
| while loop | Loops based on condition |
| break      | Exits loop early         |
| continue   | Skips current iteration  |

---

## 🔍 Prime Number Checker Program

```python
num = int(input("Enter a number: "))
if num > 1:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")
else:
    print(num, "is not a prime number")
```

---


