# SET

# 1) Create a set and add elements
s = {1, 2, 3}
s.add(4)
print("Set after adding 4:", s)

# 2) Remove element from a set
s.remove(2)
print("Set after removing 2:", s)

# 3) Union of two sets
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print("Union:", s1 | s2)

# 4) Intersection of two sets
print("Intersection:", s1 & s2)

# 5) Difference of two sets
print("Difference (s1-s2):", s1 - s2)

# 6) Symmetric difference
print("Symmetric difference:", s1 ^ s2)

# 7) Check subset or superset
s1 = {1, 2}
s2 = {1, 2, 3, 4}
print("Is s1 subset of s2?", s1.issubset(s2))
print("Is s2 superset of s1?", s2.issuperset(s1))

# 8) Remove duplicates from a list using set
lst = [1, 2, 3, 2, 4, 1, 5]
unique_lst = list(set(lst))
print("List after removing duplicates:", unique_lst)

# 9) Find common elements in multiple lists using set
l1 = [1, 2, 3, 4]
l2 = [3, 4, 5, 6]
l3 = [4, 5, 6, 7]
common = set(l1) & set(l2) & set(l3)
print("Common elements:", common)

# 10) Iterate over a set
s = {"Python", "Java", "C++"}
for lang in s:
    print("Programming language:", lang)
