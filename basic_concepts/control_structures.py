# Control Structures
# 1. If Statement
age = 18
if age >= 18:
    print("Adult")

# 2. If-Else Statement
if age < 18:
    print("Minor")
else:
    print("Adult")

# 3. Elif Statement
if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
else:
    print("Adult")

# 4. Nested If Statement
if age >= 18:
    if age < 65:
        print("Adult")
    else:
        print("Senior")

# 5. For Loop
for i in range(5):
    print(i)  # 0 1 2 3 4

# 6. For Loop with List
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 7. While Loop
count = 0
while count < 5:
    print(count)
    count += 1

# 8. Break Statement
for i in range(10):
    if i == 5:
        break
    print(i)

# 9. Continue Statement
for i in range(5):
    if i == 2:
        continue
    print(i)

# 10. Pass Statement
for i in range(3):
    if i == 1:
        pass  # do nothing
    print(i)

# 11. Range Function
for i in range(2, 10, 2):
    print(i)  # 2 4 6 8

# 12. List Comprehension
squares = [x**2 for x in range(10)]
print(squares)

# 13. Conditional Statements in List Comprehension
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)

# 14. Using Enumerate
for index, fruit in enumerate(fruits):
    print(index, fruit)

# 15. Using zip()
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 22]
for name, age in zip(names, ages):
    print(name, age)

# 16. While True Loop
while True:
    response = input("Type 'exit' to quit: ")
    if response.lower() == 'exit':
        break

# 17. Using else with For Loop
for i in range(5):
    print(i)
else:
    print("Loop finished!")

# 18. Using else with While Loop
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("While loop finished!")

# 19. Try-Except in Control Flow
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("That's not a valid number!")

# 20. Returning from Functions
def check_even(num):
    if num % 2 == 0:
        return True
    return False

print(check_even(10))  # True
