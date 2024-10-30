# Sets
# 1. Creating a Set
my_set = {1, 2, 3, 4, 5}
print(my_set)

# 2. Adding Elements
my_set.add(6)
print(my_set)

# 3. Removing Elements
my_set.discard(4)
print(my_set)

# 4. Set Union
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union_set = set_a | set_b
print(union_set)

# 5. Set Intersection
intersection_set = set_a & set_b
print(intersection_set)

# 6. Set Difference
difference_set = set_a - set_b
print(difference_set)

# 7. Checking Subset
print(set_a.issubset(union_set))

# 8. Checking Superset
print(union_set.issuperset(set_a))

# 9. Clearing a Set
my_set.clear()
print(my_set)

# 10. Checking Membership
print(2 in set_a)
