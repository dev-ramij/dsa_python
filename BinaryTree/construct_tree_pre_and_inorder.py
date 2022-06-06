class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# We will traverse through preorder array
# we will use idx for tracking the current node
# then we will find where this node is present in inorder list to determine its left and right nodes
# if there is no inorder list for the desired idx that means no node will be there in that position
# we will decrement the idx value because it is not assigned yet
# then we will create left and right tree
class Solution:
    # this is used to identify the current index of preorder
    # using -1 because we will start it from 0
    idx = -1

    def buildtree(self, inorder, preorder, n):
        if len(inorder) == 0:
            return None
        self.idx += 1
        if self.idx >= n:
            return None
        root = Node(preorder[self.idx])
        # first define inorderidx is not found
        inorderIdx = -1
        for i in range(len(inorder)):
            if inorder[i] == preorder[self.idx]:
                inorderIdx = i
                break
        # if there is no inorderIdx that means the node cannot be placed into the desired position
        if inorderIdx == -1:
            # decrement as value at idx is not assigned yet
            self.idx -=1
            return None
        # create left subtree
        root.left = self.buildtree(inorder[:inorderIdx], preorder, n)
        root.right = self.buildtree(inorder[inorderIdx + 1:], preorder, n)
        return root


ob = Solution()
ob.buildtree([1, 6, 8, 7], [1, 6, 7, 8], 4)
