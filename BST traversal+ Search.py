# Binary Search Tree (BST)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Insert a node
def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)

    return root


# Inorder Traversal: Left -> Root -> Right
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# Preorder Traversal: Root -> Left -> Right
def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


# Postorder Traversal: Left -> Right -> Root
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


# Search a value
def search(root, value):
    if root is None:
        return False

    if root.data == value:
        return True
    elif value < root.data:
        return search(root.left, value)
    else:
        return search(root.right, value)


# Main program
root = None

# Insert values
values = [50, 30, 70, 20, 40, 60, 80]

for value in values:
    root = insert(root, value)

# Traversals
print("Inorder:", end=" ")
inorder(root)

print("\nPreorder:", end=" ")
preorder(root)

print("\nPostorder:", end=" ")
postorder(root)

# Search
value = int(input("\n\nEnter value to search: "))

if search(root, value):
    print(value, "is found in BST")
else:
    print(value, "is not found in BST")
