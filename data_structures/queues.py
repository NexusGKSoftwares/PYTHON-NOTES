from collections import deque

# Queue Implementation using deque
queue = deque()

# 1. Enqueue
queue.append(1)
queue.append(2)
queue.append(3)
print("Queue after enqueues:", list(queue))

# 2. Dequeue
queue.popleft()
print("Queue after dequeue:", list(queue))

# 3. Peek
print("Front element:", queue[0])

# 4. Checking if Empty
print("Is queue empty?", len(queue) == 0)

# 5. Queue Length
print("Queue length:", len(queue))
