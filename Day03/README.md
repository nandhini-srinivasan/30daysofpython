
# Day 0️⃣3️⃣: Lists, Tuples, Dictionaries & Sets  
**Date:** May 30, 2025  

---

## What We'll Cover Today
- Lists (slicing, methods)  
- Tuples (immutability)  
- Dictionaries (key-value pairs)  
- Sets  

---

## 🎯 Challenge  
Create an inventory system that tracks items and quantities using a dictionary.

---

# 1. Lists in Python

### What is a List?  
Think of a list as a collection of items that are **ordered**, **changeable** (mutable), and can have **duplicate values**.  

```python
my_list = [10, 20, 30, 40]
```

---

### Ordered Sequences & Indexing  
Lists, tuples, strings — they’re all ordered sequences. Each item sits in a specific position called an *index*.  
- Python uses **zero-based indexing**  
- The first item is at index 0, second at 1, and so on.  

```python
print(my_list[0])   # 10 (first item)
print(my_list[-1])  # 40 (last item)
```

---

### List Slicing  
Want to grab parts of your list? Use slicing!  
Syntax: `list[start:stop:step]`

- **start**: index to start from  
- **stop**: index to stop before (exclusive)  
- **step**: how many items to skip each time  

Why stop is exclusive?  
Because it makes slicing predictable, especially when combined with `len()` and ranges. For example:  

```python
len(my_list[1:4])  # 3, because 4 - 1 = 3 items
```

Examples:  
```python
print(my_list[1:3])    # [20, 30] → index 1 to 2
print(my_list[:2])     # [10, 20]
print(my_list[::2])    # [10, 30]
print(my_list[::-1])   # [40, 30, 20, 10] → reversed list
```

---

### What Does Step Do?  
The `step` controls how Python moves through the list.

```python
fruits = ["apple", "banana", "cherry", "mango", "orange"]

# Normal slicing (step=1)
print(fruits[0:5:1])  # ['apple', 'banana', 'cherry', 'mango', 'orange']

# Skip every 2nd item
print(fruits[0:5:2])  # ['apple', 'cherry', 'orange']

# Reverse the list
print(fruits[::-1])   # ['orange', 'mango', 'cherry', 'banana', 'apple']

# Reverse a portion
print(fruits[5:1:-1]) # ['orange', 'mango', 'cherry', 'banana']
```

---

### Common List Methods  

| Method         | What It Does                       | Example                 |
|----------------|----------------------------------|-------------------------|
| `append(x)`    | Add item at the end               | `my_list.append(50)`    |
| `insert(i, x)` | Insert x at position i            | `my_list.insert(1, 15)` |
| `extend(iter)` | Add all elements of another list | `my_list.extend([60,70])`|
| `remove(x)`    | Remove first occurrence of x      | `my_list.remove(30)`    |
| `pop([i])`     | Remove and return item at index i (last if not given) | `my_list.pop(2)` |
| `clear()`      | Remove all items                  | `my_list.clear()`       |
| `index(x)`     | Return index of first occurrence  | `my_list.index(20)`     |
| `count(x)`     | Count occurrences of x            | `my_list.count(10)`     |
| `sort()`       | Sort list ascending               | `my_list.sort()`        |
| `reverse()`    | Reverse list                     | `my_list.reverse()`     |

---

# 2. Tuples in Python  

### What is a Tuple?  
Tuples are like lists but **immutable** — once created, you can't change or add to them. They are ordered and can have duplicates.

```python
my_tuple = (1, 2, 3)
print(my_tuple[0])  # 1
```

Trying to change an item causes an error:

```python
my_tuple[0] = 5  # ❌ Error! Tuples are immutable.
```

---

### Why Use Tuples?  
- When you want to make sure data *doesn't* change  
- Tuples are slightly faster than lists  
- Useful for returning multiple values from functions  

---

### Tuple Methods  

| Method      | What It Does                         | Example                   |
|-------------|------------------------------------|---------------------------|
| `count(x)`  | Count how many times x appears      | `my_tuple.count(2)`       |
| `index(x)`  | Find index of first occurrence      | `my_tuple.index(3)`       |

---

# 3. Dictionaries in Python  

### What is a Dictionary?  
A dictionary stores **key-value pairs**. It’s mutable and keys are unique. Before Python 3.7, dictionaries were unordered; now they maintain insertion order.

```python
person = {
    "name": "Nandhini",
    "age": 23
}
```

---

### Accessing & Updating  

```python
print(person["name"])          # Nandhini
print(person.get("age"))       # 23

person["age"] = 24             # Update age
person["email"] = "me@email.com"  # Add new key-value
```

---

### Looping Through a Dictionary  

**Method 1:** Loop through keys, then get values  

```python
for key in person:
    print(key, ":", person[key])
```

Output:  
```
name : Nandhini
age : 24
email : me@email.com
```

**Method 2:** Use `.items()` to get both key and value  

```python
for key, value in person.items():
    print(key, ":", value)
```

---

### Useful Dictionary Methods  

| Method       | What It Does                    |
|--------------|--------------------------------|
| `get(key)`   | Get value safely (returns None if key doesn’t exist)  |
| `keys()`     | Returns all keys               |
| `values()`   | Returns all values             |
| `items()`    | Returns all key-value pairs    |
| `update()`   | Add or update key-value pairs  |
| `pop(key)`   | Remove key and return its value|
| `clear()`    | Remove all items               |

---

# 4. Sets in Python  

### What is a Set?  
A set is an unordered collection of **unique** items. No duplicates allowed.

```python
my_set = {1, 2, 3, 3, 2}
print(my_set)  # {1, 2, 3}  # duplicates removed
```

---

### Set Methods  

| Method       | What It Does                         |
|--------------|------------------------------------|
| `add(x)`     | Add an element                     |
| `update(it)` | Add multiple elements              |
| `remove(x)`  | Remove x (error if not found)      |
| `discard(x)` | Remove x (no error if not found)   |
| `pop()`      | Remove a random item                |
| `clear()`    | Remove all items                   |

---

### Set Operations  

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))        # {1, 2, 3, 4, 5}
print(a.intersection(b)) # {3}
print(a.difference(b))   # {1, 2}
```

---

# 📌 Final Summary Chart  

| Type     | Ordered | Mutable | Duplicates Allowed | Example               |
|----------|---------|---------|--------------------|-----------------------|
| List     | ✅ Yes  | ✅ Yes  | ✅ Yes             | `[1, 2, 2, 3]`        |
| Tuple    | ✅ Yes  | ❌ No   | ✅ Yes             | `(1, 2, 3)`           |
| Dict     | ✅ (3.7+)| ✅ Yes | ❌ Keys Unique     | `{"a": 1, "b": 2}`    |
| Set      | ❌ No   | ✅ Yes  | ❌ No              | `{1, 2, 3}`           |

---

## Self Note 
 You Made It!  


🎯 Challenge
- Create an inventory system tracking items and quantities with a dictionary
 -atteached my inventory system python code 

