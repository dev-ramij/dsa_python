class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, Key):
    # If tree is empty
    if root is None:
        node = Node(Key)
        root = node
        return 
    # if duplicate record found
    if root.data == Key:
        return
    
    # if key is lesser than root
    if root.data > Key:
        # if left is none then assign it to the left
        if root.left is None:
            node = Node(Key)
            root.left = node
        # otherwise find place in left subtree
        else:
            insert(root.left,Key)
    # same logic as left
    else:
        if root.right is None:
            node = Node(Key)
            root.right = node
        else:
            insert(root.right,Key)