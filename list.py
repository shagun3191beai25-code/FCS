# LISTS


# 1) Create a list and print
numbers = [10, 20, 30, 40, 50]
print("Original list:", numbers)

# 2) Access elements
numbers = [10, 20, 30, 40, 50]
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# 3) Add elements
numbers = [10, 20, 30, 40, 50]
numbers.append(60)  # add at end
print("After append:", numbers)

numbers.insert(2, 25)  # add at index 2
print("After insert:", numbers)

# 4) Remove elements
numbers = [10, 20, 30, 40, 50]
numbers.remove(30)
print("After remove 30:", numbers)

popped = numbers.pop()  # removes last element
print("After pop:", numbers, "Popped element:", popped)

# 5) Update elements
numbers = [10, 20, 30, 40, 50]
numbers[1] = 22
print("After updating index 1:", numbers)

# 6) Loop through a list
numbers = [10, 20, 30, 40, 50]
print("Looping through list:")
for num in numbers:
    print(num, end=' ')
print()

# 7) Sum, max, min, length
numbers = [10, 20, 30, 40, 50]
print("Sum:", sum(numbers))
print("Max:", max(numbers))
print("Min:", min(numbers))
print("Length:", len(numbers))

# 8) List comprehension
numbers = [10, 20, 30, 40, 50]
squared = [x**2 for x in numbers]
print("Squared list:", squared)

evens = [x for x in numbers if x % 2 == 0]
print("Even numbers:", evens)

# 9) 2D List
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("2D List (Matrix):")
for row in matrix:
    print(row)

# Sum of each row
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Sum of each row:")
for row in matrix:
    print(sum(row))

# Largest element in each row
matrix = [
    [1, 5, 3],
    [4, 9, 7],
    [3, 8, 9]
]
print("Largest in each row:")
for row in matrix:
    print(max(row))

# Flatten 2D list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
flat = [elem for row in matrix for elem in row]
print("Flattened 2D list:", flat)

# Count even and odd numbers in 2D list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
even_count = 0
odd_count = 0
for row in matrix:
    for el in row:
        if el % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
print("Even numbers count:", even_count)
print("Odd numbers count:", odd_count)

# 10) Merge two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged = list1 + list2
print("Merged list:", merged)

# 11) Reverse a list
numbers = [10, 20, 30, 40, 50]
numbers.reverse()
print("Reversed list:", numbers)

# 12) Sort a list
numbers = [10, 20, 30, 40, 50]
numbers.sort()
print("Sorted list:", numbers)

# 13) Remove duplicates
nums = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(nums))
print("Unique elements:", unique)

# 14) Find index of element
numbers = [10, 20, 30, 40, 50]
print("Index of 22 in numbers:", numbers.index(22))

# 15) Check membership
numbers = [10, 20, 30, 40, 50]
if 22 in numbers:
    print("22 is in numbers list")
else:
    print("22 is not in numbers list")

