
# Day 03: Lists, Tuples, Dictionaries & Sets in Python  
**Date:** May 30, 2025

---

## Topics Covered  
- Lists (slicing, methods)  
- Tuples (immutability)  
- Dictionaries (key-value pairs)  
- Sets  

---

## What is a List?  
A **list** is a collection of items that are **ordered**, **changeable (mutable)**, and allow **duplicate values**.

### Creating a List
```python
my_list = [10, 20, 30, 40]
```

### Indexing

* Python uses **zero-based indexing**.
* The first element is at index 0.

```python
print(my_list[0])   # Output: 10  
print(my_list[-1])  # Output: 40 (last item)
```

### List Slicing

Syntax: `list[start:stop:step]`

* **start**: index to start from (inclusive)
* **stop**: index to stop before (exclusive)
* **step**: how many items to skip

Examples:

```python
print(my_list[1:3])    # Output: [20, 30]  (indexes 1 and 2)
print(my_list[:2])     # Output: [10, 20]
print(my_list[::2])    # Output: [10, 30]
print(my_list[::-1])   # Output: [40, 30, 20, 10]  (reversed)
```

**Note:** The half-open interval `[start:stop)` excludes the stop index, making lengths predictable.

### Step Parameter Examples

```python
fruits = ["apple", "banana", "cherry", "mango", "orange"]

print(fruits[0:5:1])  # ['apple', 'banana', 'cherry', 'mango', 'orange']  
print(fruits[0:5:2])  # ['apple', 'cherry', 'orange']  
print(fruits[::-1])   # ['orange', 'mango', 'cherry', 'banana', 'apple']  
print(fruits[5:1:-1]) # Reverse from index 5 to 2 (exclusive)  
print(fruits[0::3])   # ['apple', 'mango']
```

---

### List Methods

| Method        | Description                         | Example                   |
| ------------- | ----------------------------------- | ------------------------- |
| `append(x)`   | Add item at the end                 | `my_list.append(50)`      |
| `insert(i,x)` | Insert `x` at position `i`          | `my_list.insert(1,15)`    |
| `extend(lst)` | Add elements of another list        | `my_list.extend([60,70])` |
| `remove(x)`   | Remove first occurrence of `x`      | `my_list.remove(30)`      |
| `pop(i)`      | Remove and return item at index `i` | `my_list.pop(2)`          |
| `clear()`     | Remove all items                    | `my_list.clear()`         |
| `index(x)`    | Return index of first occurrence    | `my_list.index(20)`       |
| `count(x)`    | Count occurrences of `x`            | `my_list.count(10)`       |
| `sort()`      | Sort list in ascending order        | `my_list.sort()`          |
| `reverse()`   | Reverse the list                    | `my_list.reverse()`       |

---

## Tuples

* A **tuple** is ordered, **immutable** (cannot be changed), and allows duplicates.
* Once created, you cannot modify or add items.

### Creating a Tuple

```python
my_tuple = (1, 2, 3)
```

### Accessing Items

```python
print(my_tuple[0])  # Output: 1
```

### Immutability

```python
my_tuple[0] = 5  # ❌ This will raise an error!
```

### Tuple Methods

| Method     | Description                       | Example             |
| ---------- | --------------------------------- | ------------------- |
| `count(x)` | Count number of times `x` appears | `my_tuple.count(2)` |
| `index(x)` | Find index of first occurrence    | `my_tuple.index(3)` |

---

## Dictionaries

* A **dictionary** is a collection of **key-value pairs**.
* It is mutable and keys must be unique.
* Dictionaries are ordered from Python 3.7+.

### Creating a Dictionary

```python
person = {
    "name": "Nandhini",
    "age": 23
}
```

### Accessing and Updating

```python
print(person["name"])          # Output: Nandhini
print(person.get("age"))       # Output: 23
person["age"] = 24             # Update age
person["email"] = "me@email.com"  # Add new key-value
```

### Looping Through a Dictionary

**Method 1: Loop over keys**

```python
for key in person:
    print(key, ":", person[key])
```

**Method 2: Loop over items (key and value)**

```python
for key, value in person.items():
    print(key, ":", value)
```

### Dictionary Methods

| Method     | Description                     |
| ---------- | ------------------------------- |
| `get(key)` | Get value safely                |
| `keys()`   | Return all keys                 |
| `values()` | Return all values               |
| `items()`  | Return key-value pairs          |
| `update()` | Add or update key-value pairs   |
| `pop(key)` | Remove key and return its value |
| `clear()`  | Remove all items                |

---

## Sets

* A **set** is a collection of **unique**, **unordered** items.

### Creating a Set

```python
my_set = {1, 2, 3, 3, 2}
print(my_set)  # Output: {1, 2, 3}
```

### Set Methods

| Method        | Description                     |
| ------------- | ------------------------------- |
| `add(x)`      | Add item `x` to the set         |
| `update(lst)` | Add multiple elements           |
| `remove(x)`   | Remove `x`, error if not found  |
| `discard(x)`  | Remove `x`, no error if missing |
| `pop()`       | Remove and return a random item |
| `clear()`     | Remove all items                |

### Set Operations

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))        # Output: {1, 2, 3, 4, 5}
print(a.intersection(b)) # Output: {3}
print(a.difference(b))   # Output: {1, 2}
```

---

## Summary Chart

| Type       | Ordered    | Mutable | Allows Duplicates | Example            |
| ---------- | ---------- | ------- | ----------------- | ------------------ |
| List       | Yes        | Yes     | Yes               | `[1, 2, 2, 3]`     |
| Tuple      | Yes        | No      | Yes               | `(1, 2, 3)`        |
| Dictionary | Yes (3.7+) | Yes     | No (keys unique)  | `{"a": 1, "b": 2}` |
| Set        | No         | Yes     | No                | `{1, 2, 3}`        |

---

## 🎯 Challenge: Inventory System Tracking Items and Quantities (Using Dictionary)

```python
# List of available school supplies
available_items = ["Pencil", "Eraser", "Notebook", "Ruler", "Crayons"]

# Inventory dictionary
inventory = {}

# Program loop
while True:
    print("\n--- 📚 School Supplies Inventory ---")
    print("Available items: ", ", ".join(available_items))
    print("1. Add Item")
    print("2. View Inventory")
    print("3. Remove Item")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    # Add item
    if choice == '1':
        item = input("Enter item name from the list above: ").capitalize()
        if item not in available_items:
            print("❗Item not in available list.")
            continue
        quantity = int(input("Enter quantity: "))
        if item in inventory:
            inventory[item] += quantity
        else:
            inventory[item] = quantity
        print(f"✅ {quantity} {item}(s) added. Total: {inventory[item]}")

    # View inventory
    elif choice == '2':
        print("\n📋 Current Inventory:")
        if not inventory:
            print("Inventory is empty.")
        else:
            for item, qty in inventory.items():
                print(f"- {item}: {qty}")

    # Remove item
    elif choice == '3':
        item = input("Enter item name to remove: ").capitalize()
        if item in inventory:
            del inventory[item]
            print(f"❌ {item} removed from inventory.")
        else:
            print(f"⚠️ {item} not found.")

    # Exit
    elif choice == '4':
        print("👋 Exiting the program. Bye!")
        break

    else:
        print("Please enter a valid option (1-4).")
```

---

**Happy Coding!** 🚀
