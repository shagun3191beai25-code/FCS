# Program 1: Word frequency
sentence = input("Enter sentence: ").split()
freq = {}

for word in sentence:
    freq[word] = freq.get(word, 0) + 1

print(freq)

# Program 2: Student marks dictionary
students = {"Amit": 85, "Neha": 90, "Ravi": 78}
print("Highest marks =", max(students, key=students.get))

# Program 3: Merge Two Nested Dictionaries
d1 = {'IT': {'Amit': 50000}, 'HR': {'Riya': 40000}}
d2 = {'IT': {'Neha': 60000}, 'Sales': {'Karan': 30000}}

new = {}
for key, val in d1.items():
    new[key] = val

for key, val in d2.items():
    if key in new:
        new[key].update(val)
    else:
        new[key] = val

print(new)

# Program 4: Merge Dictionaries Without Overwriting Existing Keys
d1 = {'a': 1, 'b': 2}
d2 = {'b': 20, 'c': 3}

new = {}
for key, val in d1.items():
    new[key] = val

for key, val in d2.items():
    new.setdefault(key, val)

print(new)

# Program 5: Merge Dictionaries with Conditional Filtering
d1 = {'a': 40, 'b': 60}
d2 = {'a': 20, 'c': 70}

new = {}
for key in set(d1) | set(d2):
    total = d1.get(key, 0) + d2.get(key, 0)
    if total >= 50:
        new[key] = total

print(new)

# Program 6: Merge Dictionaries Taking Maximum Value
d1 = {'a': 10, 'b': 50, 'c': 30}
d2 = {'b': 40, 'c': 60, 'd': 20}

new = {}
for key in set(d1) | set(d2):
    new[key] = max(d1.get(key, 0), d2.get(key, 0))

print(new)

# Program 7: Merge Dictionaries with String Concatenation
d1 = {'a': 'hello', 'b': 'good'}
d2 = {'b': 'morning', 'c': 'world'}

new = {}
for key in set(d1) | set(d2):
    if key in d1 and key in d2:
        new[key] = d1[key] + " " + d2[key]
    else:
        new[key] = d1.get(key, d2.get(key))

print(new)

# Program 8: Group Keys by Their Values
data = {'Amit': 'IT', 'Riya': 'HR', 'Karan': 'IT'}

new = {}
for key, val in data.items():
    new.setdefault(val, []).append(key)

print(new)

#  Program 9: Find Key with Maximum Value
marks = {"Amit": 78, "Riya": 95, "Neha": 88, "Sumit": 91}

max_key = max(marks, key=marks.get)
print(max_key)

# Program 10: Update Inventory Count
fruits = {"apple": 50, "banana": 40, "mango": 30, "orange": 25}
sold_fruit = "banana"
sold_qty = 10

if sold_fruit in fruits:
    fruits[sold_fruit] -= sold_qty

print(fruits)
