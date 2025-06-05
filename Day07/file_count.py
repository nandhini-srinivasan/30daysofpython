
# Day 07 - Count Word Frequencies from a Text File

import string

# Step 1: Read the text file
with open("sample.txt", "r") as file:
    content = file.read()

# Step 2: Clean the text
content = content.lower()  # Convert to lowercase
for char in string.punctuation:
    content = content.replace(char, "")  # Remove punctuation

# Step 3: Split into words
words = content.split()

# Step 4: Count word frequencies
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Step 5: Display result
print("📊 Word Frequency Count:\n")
for word, count in word_count.items():
    print(f"{word}: {count}")



 Sample sample.txt File :

from indian data club, python challenge.
im learning python. python feels so natural language.
data loves python
