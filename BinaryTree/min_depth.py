
class Solution:
    def minDepth(self, root):
        #Code here
        if root is None:
            return 0
        leftHeight = self.minDepth(root.left)
        rightHeight =self.minDepth(root.right)
        # check for various condition if any of height is zero then have to return non-zero height
        if leftHeight == 0 and rightHeight ==0:
            return 1
        elif leftHeight > 0 and rightHeight == 0:
            return leftHeight+1
        elif rightHeight > 0 and leftHeight == 0:
            return rightHeight +1
        else:
            return min(leftHeight,rightHeight) +1