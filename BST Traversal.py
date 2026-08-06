# Binary Search Tree Node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# BST Class
class BST:
    def __init__(self):
        self.root = None

    # Insert a node
    def insert(self, root, key):
        if root is None:
            return Node(key)

        if key < root.data:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        return root

    # Inorder Traversal (Left -> Root -> Right)
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    # Preorder Traversal (Root -> Left -> Right)
    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    # Postorder Traversal (Left -> Right -> Root)
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")


# Driver Code
bst = BST()

# Insert elements
values = [50, 30, 70, 20, 40, 60, 80]

for value in values:
    bst.root = bst.insert(bst.root, value)

# Display Traversals
print("Inorder Traversal:")
bst.inorder(bst.root)

print("\nPreorder Traversal:")
bst.preorder(bst.root)

print("\nPostorder Traversal:")
bst.postorder(bst.root)
