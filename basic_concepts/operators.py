# Operators
# 1. Arithmetic Operators
a = 10
b = 5
print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division
print(a % b)  # Modulus
print(a ** b)  # Exponentiation
print(a // b)  # Floor Division

# 2. Comparison Operators
print(a > b)   # Greater than
print(a < b)   # Less than
print(a == b)  # Equal to
print(a != b)  # Not equal to
print(a >= b)  # Greater than or equal to
print(a <= b)  # Less than or equal to

# 3. Logical Operators
x = True
y = False
print(x and y)  # Logical AND
print(x or y)   # Logical OR
print(not x)    # Logical NOT

# 4. Bitwise Operators
print(a & b)  # Bitwise AND
print(a | b)  # Bitwise OR
print(a ^ b)  # Bitwise XOR
print(~a)     # Bitwise NOT
print(a << 1) # Left Shift
print(a >> 1) # Right Shift

# 5. Assignment Operators
c = 10
c += 5  # c = c + 5
print(c)
c *= 2  # c = c * 2
print(c)

# 6. Identity Operators
list1 = [1, 2, 3]
list2 = list1
list3 = list1[:]
print(list1 is list2)  # True
print(list1 is list3)  # False

# 7. Membership Operators
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)   # True
print(6 not in my_list) # True

# 8. Precedence of Operators
result = 10 + 5 * 2
print(result)  # 20

# 9. Chaining Comparison
a, b, c = 5, 10, 15
print(a < b < c)  # True

# 10. Ternary Operator
max_num = a if a > b else b
print(max_num)  # 10

# 11. Modulus with Negative Numbers
print(-10 % 3)  # 2

# 12. Floor Division with Negative Numbers
print(-10 // 3)  # -4

# 13. String Concatenation Using `+`
str1 = "Hello, "
str2 = "World!"
print(str1 + str2)

# 14. Using `+=` for Strings
str1 += "Python"
print(str1)

# 15. Logical Expressions
print((a > 5) and (b < 15))

# 16. Combining Logical and Comparison
print((a > 5) or (b > 15))

# 17. Nested Operations
result = (10 + 5) * 2
print(result)

# 18. Using `abs()` with Arithmetic Operators
negative_number = -5
print(abs(negative_number))

# 19. Using `pow()` function
print(pow(2, 3))  # 8

# 20. Using `round()` function
print(round(3.14159, 2))  # 3.14
