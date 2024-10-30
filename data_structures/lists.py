# Lists
# 1. Creating a List
my_list = [1, 2, 3, 4, 5]
print(my_list)

# 2. Accessing Elements
print(my_list[0])  # First element
print(my_list[-1])  # Last element

# 3. Slicing
print(my_list[1:3])  # Elements from index 1 to 2

# 4. Appending Elements
my_list.append(6)
print(my_list)

# 5. Removing Elements
my_list.remove(3)
print(my_list)

# 6. List Comprehension
squares = [x ** 2 for x in my_list]
print(squares)

# 7. Checking Membership
print(2 in my_list)

# 8. Sorting a List
my_list.sort(reverse=True)
print(my_list)

# 9. Reversing a List
my_list.reverse()
print(my_list)

# 10. Counting Elements
print(my_list.count(2))
