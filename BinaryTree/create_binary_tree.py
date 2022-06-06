class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:

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

    def getSize(self, root):
        if root is None:
            return 0
        return self.getSize(root.left) + self.getSize(root.right) + 1
    
    def maximumSize(self, root):
        if root is None:
            return 0
        return max(root.data,max(self.maximumSize(root.left),self.maximumSize(root.right)))


tree = BinaryTree()
root = tree.createBinaryTree()
print(tree.getSize(root))
print(tree.maximumSize(root))
