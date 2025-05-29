# 🐍 Python Variables for Beginners – Day 2

Hey there! 👋  
Welcome to **Day 2** of my Python learning journey.

Today, I explored the basics of **variables** in Python — how they work, how to use them, and the different data types like **integers**, **floats**, **strings**, and **booleans**.

🎥 I followed along with this amazing YouTube video that explained things really well:  
[🔗 Python Variables Are Easy – by BroCode](https://youtu.be/LKFrQXaoSMQ?si=uvqXFUyLj9-Xgmtk)

And yes... I also completed the **Area Finding Challenge** at the end of the video! 🙌  
(Let's just say I had to rewind a few times 😅 but it was worth it!)

---

## 🧠 What I Learned

### 🔁 Variables

A variable is like a container that stores a value.

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

### ➕ String Concatenation

```python
age = 21
print("You are " + str(age) + " years old")     # using str()
print("You are", age, "years old")              # using commas
print(f"You are {age} years old")               # f-string (my fav!)
```

---

### 🔢 Integer

```python
x = 5
y = -10
z = 0

print(type(x))  # <class 'int'>
```

Convert string or float to int:

```python
a = int("25")
b = int(3.9)  # becomes 3
```

---

### 🌊 Float

A number with decimals:

```python
gpa = 3.2
distance = 2.5
price = 10.99

print(f"Your GPA is {gpa}, and you run {distance} km daily")
```

Convert int to float:

```python
x = 10
print(float(x))  # 10.0
```

Convert float to int:

```python
z = int(10.75)
print(z)  # 10
```

---

### 🧵 String Basics

```python
name = "Nandhini"
greeting = 'Hello, world!'
multiline = """This is
a multi-line
string."""
```

**String operations I tried:**

```python
full_name = "Nand" + "hini"
echo = "Hi! " * 3

print(full_name)  # Nandhini
print(echo)       # Hi! Hi! Hi!
```

Accessing characters:

```python
first_char = name[0]
last_char = name[-1]
print(first_char, last_char)
```

---

### 💬 Common String Methods

```python
s = " Hello World! "

print(s.lower())                      # ' hello world! '
print(s.upper())                      # ' HELLO WORLD! '
print(s.strip())                      # 'Hello World!'
print(s.replace("World", "Python"))   # ' Hello Python! '
print(s.split())                      # ['Hello', 'World!']
print(s.startswith(" He"))            # True
print(s.endswith("! "))               # True
```

Fun example:

```python
name = "Bro"
food = "pizza"
email = "Bro123@gmail.com"

print(f"I'm {name} and I love {food}, you can send mail about your new {food} offers to my mail {email}")
```

---

### ✅ Boolean

```python
is_active = True
is_logged_in = False
print(type(is_active))  # <class 'bool'>
```

**Comparisons:**

```python
x = 10
y = 5

print(x > y)     # True
print(x == y)    # False
print(x != y)    # True
```

**Logical operators:**

```python
a = True
b = False

print(a and b)   # False
print(a or b)    # True
print(not a)     # False
```

**Used in conditions:**

```python
age = 20
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

---

### ⚠️ Falsy Values in Python

Python treats the following as `False` in conditions:

- `0`
- `0.0`
- `''` (empty string)
- `[]`, `{}`, `()` (empty collections)
- `None`

Everything else is considered `True`.

> 🔎 Reminder: Boolean values must be without quotes — `"True"` becomes a string!

---

💪 Looking forward to **Day 3** already! Let’s keep going 🚀

