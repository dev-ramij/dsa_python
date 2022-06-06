class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Traversal:

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

    #left,root,right
    def inOrder(self, root):
        if root is None:
            return
        self.inOrder(root.left)
        print(root.data)
        self.inOrder(root.right)
    
    #root,left,right
    def preOrder(self, root):
        if root is None:
            return
        print(root.data)
        self.preOrder(root.left)
        self.preOrder(root.right)
    
    #left,right,root
    def postOrder(self, root):
        if root is None:
            return
        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.data)
        


ob = Traversal()
root = ob.createBinaryTree()
ob.inOrder(root)
print("&&&")
ob.preOrder(root)
print("&&&")
ob.postOrder(root)
