# STRING

# 1) Reverse a string
s = "Python"
reversed_s = s[::-1]
print("Reversed string:", reversed_s)

# 2) Count vowels in a string
s = "Hello Python"
vowels = "aeiouAEIOU"
count = sum(1 for char in s if char in vowels)
print("Number of vowels:", count)

# 3) Check palindrome
s = "racecar"
if s == s[::-1]:
    print(s, "is a palindrome")
else:
    print(s, "is not a palindrome")

# 4) Count words in a sentence
sentence = "Python is easy and powerful"
words = sentence.split()
print("Number of words:", len(words))

# 5) Convert string to uppercase and lowercase
s = "Hello World"
print("Uppercase:", s.upper())
print("Lowercase:", s.lower())

# 6) Find frequency of each character
s = "programming"
freq = {}
for char in s:
    freq[char] = freq.get(char, 0) + 1
print("Character frequency:", freq)

# 7) Replace substring
s = "I love Java"
new_s = s.replace("Java", "Python")
print(new_s)

# 8) Check if string contains only digits
s = "12345"
print("Is digit?", s.isdigit())

# 9) Check if string starts with or ends with a substring
s = "Python2026"
print("Starts with 'Python'?", s.startswith("Python"))
print("Ends with '26'?", s.endswith("26"))

# 10) Find first and last occurrence of a character
s = "hello world"
print("First occurrence of 'l':", s.find('l'))
print("Last occurrence of 'l':", s.rfind('l'))

