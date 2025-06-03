# Day4 Control Structures: if-else, Loops, break & continue

**Date:** May 31, 2025

🎯 \*\*Challenge \*\*- Check if a user-entered number is prime

## 1. If-Else Statements

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

**Output:** `You are eligible to vote!`

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

**Output:** `Grade B`

---

## 2. Loops in Python

Loops repeat a block of code multiple times.

### 🔸 For Loop

Used to iterate over a sequence (like list, string, etc.)

#### ✅ Example 1: Loop Through a List

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

**Output:**

```
apple
banana
cherry
```

#### ✅ Example 2: Using range()

```python
for i in range(1, 6):
    print(i)
```

**Output:**

```
1
2
3
4
5
```

### 🔸 While Loop

Repeats as long as a condition is True.

#### ✅ Example:

```python
count = 1
while count <= 5:
    print("Count is:", count)
    count += 1
```

**Output:**

```
Count is: 1
Count is: 2
Count is: 3
Count is: 4
Count is: 5
```

### 🔸 else with Loops

Python allows `else` with loops — runs only if loop doesn't hit a `break`.

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

## Nested Loops

Loops inside loops — useful for grids, patterns, matrix operations.

### ✅ Example: Print a 3x3 Grid

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
```

**Output:**

```
1 1
1 2
1 3
2 1
2 2
2 3
3 1
3 2
3 3
```

---

## ⚠️ Infinite Loop

Use only when you plan to `break` manually.

```python
while True:
    print("This runs forever unless you break it.")
```

---

## 3. break and continue

### 🔸 `break` — Exits the loop immediately

### 🔸 `continue` — Skips current iteration, moves to next

### ✅ Example 1: Using break

```python
for i in range(1, 10):
    if i == 5:
        break
    print(i)
```

**Output:**

```
1
2
3
4
```

#### 🍬 Candy Example:

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

**Output:**

```
1
2
4
5
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

## 🔔 Note: Indentation in Python

Indentation defines blocks of code. Wrong indentation = Error!

```python
if True:
    print("Correct")  # ✅ Properly indented
  # print("Wrong")    # ❌ Will cause an error
```

---

## Summary Table

| Concept    | Use Case                 |
| ---------- | ------------------------ |
| if-else    | Make decisions           |
| for loop   | Loop through sequences   |
| while loop | Loop based on conditions |
| break      | Exit the loop early      |
| continue   | Skip current iteration   |

---

## Challenge: Prime Number Program

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
