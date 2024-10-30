# Stack Implementation using List
stack = []

# 1. Push
stack.append(1)
stack.append(2)
stack.append(3)
print("Stack after pushes:", stack)

# 2. Pop
stack.pop()
print("Stack after pop:", stack)

# 3. Peek
print("Top element:", stack[-1])

# 4. Checking if Empty
print("Is stack empty?", len(stack) == 0)

# 5. Stack Length
print("Stack length:", len(stack))
