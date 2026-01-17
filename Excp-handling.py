# Exception Handling in Python

# 1. Basic try-except
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# 2. Multiple except blocks
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Division by zero is not allowed.")

# 3. try-except-else-finally
try:
    a = 10
    b = 2
    c = a / b
except ZeroDivisionError:
    print("Division error")
else:
    print("Result:", c)
finally:
    print("Execution completed")

# 4. Handling IndexError
try:
    lst = [1, 2, 3]
    print(lst[5])
except IndexError:
    print("Index out of range")

# 5. Raising a built-in exception
value = int(input("Enter value: "))
if value > 100:
    raise ValueError("Value must be 100 or less")
else:
    print("Valid value entered")

# 6. User-defined exception
class AgeError(Exception):
    pass

try:
    age = int(input("Enter age: "))
    if age < 18:
        raise AgeError("Age must be 18 or above")
except AgeError as e:
    print(e)
else:
    print("Access granted")

# 7. finally block with return
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    finally:
        print("Operation finished")

print(divide(10, 2))
print(divide(10, 0))
