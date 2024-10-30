# Dictionaries
# 1. Creating a Dictionary
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
print(my_dict)

# 2. Accessing Values
print(my_dict['name'])

# 3. Adding Key-Value Pairs
my_dict['country'] = 'USA'
print(my_dict)

# 4. Removing Key-Value Pairs
del my_dict['age']
print(my_dict)

# 5. Checking Keys
print('name' in my_dict)

# 6. Looping through Keys and Values
for key, value in my_dict.items():
    print(key, value)

# 7. Dictionary Comprehension
squared_numbers = {x: x ** 2 for x in range(5)}
print(squared_numbers)

# 8. Merging Dictionaries
my_dict.update({'age': 30, 'job': 'Developer'})
print(my_dict)

# 9. Getting All Keys and Values
print(list(my_dict.keys()))
print(list(my_dict.values()))

# 10. Clearing a Dictionary
my_dict.clear()
print(my_dict)
