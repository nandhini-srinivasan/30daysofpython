
---


# 📚 Day 07 – File Handling in Python (My Learning Notes)

🗓️ Date: June 3, 2025  
👩‍💻 From: #IDC30DaysChallenge (Indian Data Club)  
🧠 Theme: Reading, writing, and analyzing files with Python

---

## ✨ What I Learned Today

Today I explored **file handling** in Python — how to read and write text files, clean text data, work with `.csv` files, and even build a small text analysis project.  

Even though I didn’t stick to the schedule perfectly, I showed up today to keep learning. One day at a time 💪

---

## 📂 Topics Covered

### 🔸 1. Opening a File

```python
file = open("example.txt", "r")  # open file in read mode
````

**Modes I learned:**

| Mode | Description                      |
| ---- | -------------------------------- |
| `r`  | Read (default)                   |
| `w`  | Write (overwrites file)          |
| `a`  | Append (add to existing content) |
| `x`  | Create (fails if file exists)    |
| `b`  | Binary mode                      |
| `t`  | Text mode (default)              |

---

### 🔸 2. Reading a File

```python
file = open("sample.txt", "r")
print(file.read())
file.close()
```

Or the better way using `with`:

```python
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)
```

✅ **Learning**: `with open(...)` automatically closes the file.

---

### 🔸 3. Writing to a File

```python
with open("output.txt", "w") as file:
    file.write("Learning Python is fun!\n")
```

✅ **Note**: `"w"` mode overwrites the existing content.

---

### 🔸 4. Appending to a File

```python
with open("output.txt", "a") as file:
    file.write("Adding this line at the end.\n")
```

✅ **Learning**: `"a"` mode adds content without erasing what's already there.

---

### 🔸 5. Reading Line by Line

```python
with open("sample.txt", "r") as file:
    for line in file:
        print(line.strip())
```

---

### 🔸 6. Reading a CSV File

```python
import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

✅ **Learning**: `csv.reader()` reads comma-separated values as lists.

---

## 💡 Mini Project: Count Word Frequencies

📄 Text in `sample.txt`:

```
from indian data club, python challenge.
im learning python. python feels so natural language.
data loves python
```

### 🔹 Step 1: Read the File

```python
with open("sample.txt", "r") as file:
    content = file.read()
```

---

### 🔹 Step 2: Clean and Split the Text

```python
import string

content = content.lower()
for char in string.punctuation:
    content = content.replace(char, "")

words = content.split()
print(words)
```

---

### 🔹 Step 3: Count Word Frequencies

```python
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)
```

---

### ✅ Output

```python
{
  'from': 1,
  'indian': 1,
  'data': 2,
  'club': 1,
  'python': 4,
  'challenge': 1,
  'im': 1,
  'learning': 1,
  'feels': 1,
  'so': 1,
  'natural': 1,
  'language': 1,
  'loves': 1
}
```

---

## 💬 Reflection

I didn’t follow the streak exactly, but I reminded myself — **progress over perfection**.
Even one step counts when you're trying to grow.

This task helped me see how useful Python is in real-world text processing, and how something simple like reading a file can lead to meaningful data insights.
And honestly, Python *does* feel like natural language. 😄🐍

---




