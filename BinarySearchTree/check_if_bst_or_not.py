# Inorder traversal of BST always will be a sorted array
# so if check prev value is greater then it is not a BST
class Solution:
    # flag will be false if bst is not valid
    flag = True
    # set to - infinity
    prev = -99999999999

    def inOrder(self, root):
        if root is None or self.flag == False:
            return None
        self.inOrder(root.left)
        if self.prev > root.data:
            self.flag = False
        else:
            self.prev = root.data
        self.inOrder(root.right)

    def isBST(self, root):
        self.inOrder(root)
        return self.flag
