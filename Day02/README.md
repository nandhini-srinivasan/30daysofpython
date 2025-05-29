# 🐍 Python Variables for Beginners

> Notes and examples to help beginners understand Python variables and basic data types.

---

## 📌 Variables

- A **variable** is a reusable container for storing a value.
- It behaves as if it were the value it contains.

```python
x = 3
print(2 + x)  # Output: 5
```

You can assign multiple variables in one line:

```python
x, y, z = 1, 2, 3
a = b = c = 2
```

---

## 🔤 String Concatenation

```python
age = 21
# Error: Cannot concatenate string with int directly
# print("You are " + age + " years old")

# Correct ways:
print("You are " + str(age) + " years old")
print("You are", age, "years old")
print(f"You are {age} years old")
```

---

## 🔢 Integer

An **integer** is a whole number without a decimal.

```python
x = 5
y = -10
z = 0
```

```python
age = 21
players = 2
quantity = 5

print(f"You are {age} years old")
print(f"There are {players} players online")
print(f"You would like to buy {quantity} items")
```

**Check variable type:**

```python
print(type(x))  # <class 'int'>
```

**Convert types:**

```python
a = int("25")  # string to int
b = int(3.9)   # float to int (result: 3)
```

---

## 🌊 Float

A **float** is a number with a decimal point.

```python
a = 10.5
b = 2.0

print(a + b)  # 12.5
print(a - b)  # 8.5
print(a * b)  # 21.0
print(a / b)  # 5.25
```

**Convert int to float:**

```python
x = 10
print(float(x))  # 10.0
```

**Convert float to int:**

```python
z = int(10.75)
print(z)  # 10
```

Example:

```python
gpa = 3.2
distance = 2.5
print(f"Your GPA is {gpa}, and you run {distance} km daily")
```

---

## 🧵 String

Strings are sequences of characters in quotes.

```python
name = "Nandhini"
greeting = 'Hello, world!'
multiline = """This is
a multi-line
string."""
```

**Operations:**

```python
full_name = "Nand" + "hini"  # Concatenation
echo = "Hi! " * 3            # Repetition

first_char = name[0]         # 'N'
last_char = name[-1]         # 'i'
sub = name[0:4]              # 'Nand'

length = len(name)           # 8
```

**Common methods:**

```python
s = " Hello World! "

print(s.lower())
print(s.upper())
print(s.strip())
print(s.replace("World", "Python"))
print(s.split())
print(s.startswith(" He"))
print(s.endswith("! "))
```

Example:

```python
name = "Bro"
food = "pizza"
email = "Bro123@gmail.com"

print(f"I'm {name} and I love {food}, you can send mail about your new {food} offers to my mail {email}")
```

---

## ✅ Boolean

- A **Boolean** can be `True` or `False`.

```python
is_active = True
is_logged_in = False

print(type(is_active))  # <class 'bool'>
```

**Comparison:**

```python
x = 10
y = 5

print(x > y)    # True
print(x == y)   # False
print(x != y)   # True
```

**Logical Operators:**

```python
a = True
b = False

print(a and b)  # False
print(a or b)   # True
print(not a)    # False
```

**In conditions:**

```python
age = 20
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

---

## ⚠️ Falsy Values in Python

In conditions, Python treats the following as `False`:
- `0`
- `0.0`
- `''` (empty string)
- `[]`, `{}`, `()` (empty collections)
- `None`

> Everything else is considered `True`.

**Important:**  
Don’t enclose boolean values in quotes, or they become strings.

---
