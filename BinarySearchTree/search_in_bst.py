class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:

    def createBinaryTree(self):
        print("Enter data:")
        data = int(input())
        if data == -1:
            return None
        node = Node(data)
        print("Enter the left node data for", data)
        node.left = self.createBinaryTree()
        print("Enter the right node data for", data)
        node.right = self.createBinaryTree()
        return node

    def search(self, root, element):
        # If can't find
        if root is None:
            return False
        # if data is present
        if root.data == element:
            return True
        # if root is greater then we need to search for left
        # otherwise right
        if root.data > element:
            return self.search(root.left, element)
        else:
            return self.search(root.right, element)


tree = BinarySearchTree()
root = tree.createBinaryTree()
print(tree.search(root, 15))
