import sys


class Solution:
    count = sys.maxsize

    #Function to find the least absolute difference between any node
    #value of the BST and the given integer.
    def inOrder(self, root, k):
        if root is None:
            return
        self.inOrder(root.left, k)
        # if difference is lesser then update count
        if abs(root.data - k) < self.count:
            self.count = abs(root.data - k)
        self.inOrder(root.right, k)

    def minDiff(self, root, K):
        # Do inorder traversal
        self.inOrder(root, K)
        return self.count
