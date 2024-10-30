# Functions
# 1. Basic Function Definition
def greet():
    print("Hello, World!")

greet()

# 2. Function with Parameters
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

# 3. Function with Return Value
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # 8

# 4. Default Parameters
def greet(name="World"):
    print(f"Hello, {name}!")

greet()        # Hello, World!
greet("Bob")  # Hello, Bob!

# 5. Keyword Arguments
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet(animal_type="hamster", pet_name="Harry")

# 6. Variable-Length Arguments (*args)
def print_args(*args):
    for arg in args:
        print(arg)

print_args(1, 2, 3)

# 7. Variable-Length Keyword Arguments (**kwargs)
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="Alice", age=25)

# 8. Function with List Parameter
def print_fruits(fruits):
    for fruit in fruits:
        print(fruit)

print_fruits(["apple", "banana", "cherry"])

# 9. Recursive Function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # 120

# 10. Lambda Function
add = lambda x, y: x + y
print(add(2, 3))  # 5

# 11. Function Annotations
def add(a: int, b: int) -> int:
    return a + b

print(add(3, 4))

# 12. Inner Functions
def outer_function():
    def inner_function():
        return "Hello from inner function!"
    return inner_function()

print(outer_function())

# 13. Returning Multiple Values
def get_min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = get_min_max([1, 2, 3, 4, 5])
print(minimum, maximum)  # 1 5

# 14. Closures
def outer(x):
    def inner(y):
        return x + y
    return inner

closure_function = outer(10)
print(closure_function(5))  # 15

# 15. Decorators
def decorator_function(original_function):
    def wrapper_function():
        print("Wrapper executed before {}".format(original_function.__name__))
        return original_function()
    return wrapper_function

@decorator_function
def display():
    print("Display function executed")

display()

# 16. Using *args and **kwargs Together
def print_all(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_all(1, 2, 3, name="Alice", age=25)

# 17. Function as an Argument
def apply_function(func, value):
    return func(value)

print(apply_function(lambda x: x**2, 5))  # 25

# 18. Docstrings
def example_function():
    """This function does nothing."""
    pass

print(example_function.__doc__)

# 19. Function Chaining
def multiply_by_two(x):
    return x * 2

def add_three(x):
    return x + 3

result = add_three(multiply_by_two(5))
print(result)  # 13

# 20. Function Composition
def compose(f, g):
    return lambda x: f(g(x))

square = lambda x: x**2
increment = lambda x: x + 1

composed_function = compose(increment, square)
print(composed_function(3))  # 10
