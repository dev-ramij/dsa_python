class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:

    def removekeys(self, root, l, r):
        if root is None:
            return None
        # if root is less than l then we should discard the left subtree along with root
        # because all value in left sub tree will be less than l
        # same for right subtree
        if root.data < l:
            return self.removekeys(root.right,l,r)
        if root.data > r:
            return self.removekeys(root.left,l,r)
        # if root is in range do it for left and right subtree
        root.left = self.removekeys(root.left,l,r)
        root.right = self.removekeys(root.right,l,r)
        return root
