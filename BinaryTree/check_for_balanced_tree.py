class Solution:

    def getHeights(self, root):
        if root is None:
            return 0
        return max(self.getHeights(root.left), self.getHeights(root.right)) + 1

    def isBalanced(self, root):
        if root is None:
            return 0
        leftHeight = self.getHeights(root.left)
        rightHeight = self.getHeights(root.right)
        # check if left height and right height is less than or equal 1 and also subtrees are balanced
        if abs(leftHeight - rightHeight) <= 1 and self.isBalanced(
                root.left) and self.isBalanced(root.right):
            return True
        return False