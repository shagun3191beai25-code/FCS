# LOOPS

# 1. Simple while loop with break
i = 1
while i <= 10:
    print(i)
    i += 1
    if i == 5:
        break
print("End loop")

# 2. While loop with continue
i = 0
while i < 10:
    i += 1
    if i == 3:
        continue
    print(i)

# 3. For loop with break 
nums = [7, 2, 3, 4, 1, 2, 3]
for num in nums:
    print(num)
    if num == 4:
        break

# 4. While loop with break 
count = 0
nums = [7, 2, 3, 4, 1, 2, 3]
while count < len(nums):
    print(nums[count])
    if nums[count] == 4:
        break
    count += 1
print("End of loop")

# 5. For loop over string
for ch in "Hellopython":
    print(ch)
    if ch == "p":
        break


# 6. Print numbers from 1 to 10
for i in range(1, 11):
    print(i)

# 7. Sum of first n numbers
n = int(input("Enter n: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Sum =", total)

# 8. Reverse a number
num = int(input("Enter number: "))
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10
print("Reversed number =", rev)
