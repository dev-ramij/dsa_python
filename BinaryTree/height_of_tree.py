class Tree:

    def getHeight(self, root):
        if root is None:
            return 0
        # check which's height is max left or right then add one for the root itself
        return max(self.getHeight(root.left), self.getHeight(root.right)) + 1
