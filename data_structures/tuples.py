# Tuples
# 1. Creating a Tuple
my_tuple = (1, 2, 3)
print(my_tuple)

# 2. Accessing Elements
print(my_tuple[0])

# 3. Tuple Unpacking
a, b, c = my_tuple
print(a, b, c)

# 4. Single Element Tuple
single_element = (5,)
print(single_element)

# 5. Checking Membership
print(2 in my_tuple)

# 6. Counting Elements
print(my_tuple.count(1))

# 7. Index of Element
print(my_tuple.index(2))

# 8. Converting Tuple to List
my_list = list(my_tuple)
print(my_list)

# 9. Concatenating Tuples
tuple_concat = my_tuple + (4, 5)
print(tuple_concat)

# 10. Nesting Tuples
nested_tuple = ((1, 2), (3, 4))
print(nested_tuple)
