# IF-ELSE & DECISION MAKING PROGRAMS 

# 1. Check if a number is positive, negative, or zero
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# 2. Check even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 3. Largest of three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
    print("Largest is:", a)
elif b >= a and b >= c:
    print("Largest is:", b)
else:
    print("Largest is:", c)

# 4. Check vowel or consonant
char = input("Enter a character: ")
if char.lower() in "aeiou":
    print("It is a vowel.")
else:
    print("It is not a vowel.")

# 5. Check leap year
year = int(input("Enter year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")

# 6. Simple calculator (+, -, *, /)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")
if op == "+":
    print("Result:", a + b)
elif op == "-":
    print("Result:", a - b)
elif op == "*":
    print("Result:", a * b)
elif op == "/":
    print("Result:", a / b)
else:
    print("Invalid operator")

# 7. Grade based on marks
marks = int(input("Enter marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

# 8. FizzBuzz check
num = int(input("Enter number: "))
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)

# 9. Check traffic light instruction
color = input("Enter traffic light color: ")
match color.lower():
    case "red":
        print("Stop")
    case "yellow":
        print("Get Ready")
    case "green":
        print("Go")
    case _:
        print("Invalid color")

# 10. Check perfect square
import math
num = int(input("Enter a number: "))
root = int(math.sqrt(num))
if root * root == num:
    print(num, "is a perfect square.")
else:
    print(num, "is not a perfect square.")

# 11. Check Armstrong number (3-digit)
num = int(input("Enter a 3-digit number: "))
a = num // 100
b = (num // 10) % 10
c = num % 10
if a**3 + b**3 + c**3 == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")

# 12. Simple eligibility check for loan (nested if-else)
age = int(input("Enter age: "))
salary = int(input("Enter monthly salary: "))
experience = int(input("Enter work experience in years: "))
if age >= 21:
    if salary >= 25000:
        if experience >= 2:
            print("Eligible for loan")
        else:
            print("Not eligible: Insufficient experience")
    else:
        print("Not eligible: Low salary")
else:
    print("Not eligible: Age below 21")

# 13. Check single digit number
num = int(input("Enter a number: "))
if 1 <= num <= 9:
    print("It is a single digit number")
else:
    print("It is not a single digit number")

# 14. ATM Withdrawal Simulation
correct_pin = 1234
balance = 5000
entered_pin = int(input("Enter your PIN: "))
if entered_pin == correct_pin:
    amount = int(input("Enter withdrawal amount: "))
    if amount <= balance:
        balance -= amount
        print(f"Withdrawal successful! Remaining balance: {balance}")
    else:
        print("Error: Insufficient balance")
else:
    print("Error: Incorrect PIN")
