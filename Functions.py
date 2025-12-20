# Function to print Fibonacci series:
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
n = int(input("Enter number of terms: "))
for i in range(n):
    print(fibonacci(i))

# Function to print even,odd numbers from a list
def even_odd(lst):
    even = []
    odd = []
    for el in lst:
        if el%2 == 0:
            even.append(el)
        else:
            odd.append(el)
    print("Even:",even)
    print("Odd:",odd)
even_odd([1,2,3,4,5,6,7,8,9,10])

# Function to remove duplicates from a list
def remove_duplicates(lst):
    new_list=[]
    for el in lst:
        if el not in new_list:
            new_list.append(el)
    return new_list
print(remove_duplicates([1,2,3,2,4,4,3,2,5,6]))

# function to sort list
def sort_list(lst):
    return sorted(lst)
print(sorted([1,4,7,6,5,3,2,9]))

# function to merge list
def merge_list(l1,l2):
    return l1+l2
print(merge_list([1,3,4,5,2],[7,6,8,9,10]))

# function to search element in a list
def search_element(lst, key):
    return key in lst
print(search_element([5, 8, 1], 8))

# function to find second largest number in a list
def second_largest(lst):
    lst = list(set(lst))
    lst.sort()
    return lst[-2]
print(second_largest([10, 20, 30, 40]))

# Function to convert list to tuple
def list_to_tuple(lst):
    return tuple(lst)
print(list_to_tuple([1, 2, 3, 4]))

# Function to find length of tuple
def tuple_length(tup):
    return len(tup)
print(tuple_length((1,2,3,4,5,6)))

# Function to find union and intersection of sets
def set_union_intersection(set1, set2):
    union = set1 | set2
    intersection = set1 & set2
    return union, intersection
print(set_union_intersection({1,2,3,4,5},{4,5,6,7,8}))

# Function to count key-value pairs in dictionary
def count_dict_items(d):
    return len(d)
my_dict = {'a': 1, 'b': 2, 'c': 3}
count = count_dict_items(my_dict)
print(count)

# Function to find maximum value in dictionary
def max_dict_value(d):
    return max(d.values())
my_dict = {'a': 10, 'b': 25, 'c': 15}
maximum = max_dict_value(my_dict)
print(maximum)

# Function to sort dictionary by keys
def sort_dict_by_keys(d):
    return dict(sorted(d.items()))
my_dict = {3: 'c', 1: 'a', 2: 'b'}
sorted_dict = sort_dict_by_keys(my_dict)
print(sorted_dict)

# Function to check key existence in dictionary
def key_exists(d, key):
    return key in d
my_dict = {'x': 10, 'y': 20}
print(key_exists(my_dict, 'x'))

# Function to remove a key from dictionary
def remove_key(d, key):
    d.pop(key, None)
    return d
my_dict = {'a': 1, 'b': 2, 'c': 3}
updated_dict = remove_key(my_dict, 'b')
print(updated_dict)
