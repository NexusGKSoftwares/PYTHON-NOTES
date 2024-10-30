class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# 1. Inserting Nodes
root = Node(10)
root.left = Node(5)
root.right = Node(15)

# 2. In-Order Traversal
def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.data, end=' ')
        inorder_traversal(node.right)

# 3. Pre-Order Traversal
def preorder_traversal(node):
    if node:
        print(node.data, end=' ')
        preorder_traversal(node.left)
        preorder_traversal(node.right)

# 4. Post-Order Traversal
def postorder_traversal(node):
    if node:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.data, end=' ')

# 5. Testing Traversals
print("In-Order Traversal:")
inorder_traversal(root)
print("\nPre-Order Traversal:")
preorder_traversal(root)
print("\nPost-Order Traversal:")
postorder_traversal(root)
