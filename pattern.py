# Pattern 1: Right Angle Star Triangle
n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end="")
    print()


# Pattern 2: Inverted Right Angle Star Triangle
n = int(input())
for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print("*", end="")
    print()


# Pattern 3: Number Triangle (1 to i)
n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()


# Pattern 4: Repeating Row Number Triangle
n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(i, end="")
    print()


# Pattern 5: Continuous Number Triangle
n = int(input())
count = 0
for i in range(1, n + 1):
    for j in range(1, i + 1):
        count += 1
        print(count, end=" ")
    print()


# Pattern 6: Continuous Numbers with Row Join
n = int(input())
count = 1
for i in range(1, n + 1):
    row = []
    for j in range(i):
        row.append(str(count))
        count += 1
    print(" ".join(row))


# Pattern 7: Pyramid Star Pattern
n = int(input())
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))


# Pattern 8: Inverted Pyramid Star Pattern
n = int(input())
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))


# Pattern 9: Diamond Star Pattern
n = int(input())
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))


# Pattern 10: Hollow Pyramid Star Pattern
n = int(input())
for i in range(1, n + 1):
    if i == 1:
        print(" " * (n - i) + "*" + " " * (n - i))
    elif i == n:
        print("*" * (2 * i - 1))
    else:
        print(" " * (n - i) + "*" + " " * (2 * i - 3) + "*")


# Pattern 11: Hollow Diamond Star Pattern
n = int(input())
for i in range(1, n + 1):
    if i == 1:
        print(" " * (n - i) + "*")
    else:
        print(" " * (n - i) + "*" + " " * (2 * i - 3) + "*")
for i in range(n - 1, 0, -1):
    if i == 1:
        print(" " * (n - i) + "*")
    else:
        print(" " * (n - i) + "*" + " " * (2 * i - 3) + "*")


# Pattern 12: Hollow Number Diamond Pattern
n = int(input())

# Upper half
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    if i == 1:
        print("1")
    else:
        print("1" + " " * (2 * i - 3) + str(i))

# Lower half
for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")
    if i == 1:
        print("1")
    else:
        print("1" + " " * (2 * i - 3) + str(i))
