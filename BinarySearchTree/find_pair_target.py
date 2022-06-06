# do inorder traversal 
# store the traversed node data to a hashMap
# check if pair found or not
class Solution:
    
    founded = False

    def inOrder(self, root, target, hashMap):
        if root is None or self.founded:
            return
        self.inOrder(root.left, target, hashMap)
        remaining = target - root.data
        if remaining in hashMap:
            self.founded = True
            return
        hashMap[root.data] = 1
        self.inOrder(root.right, target, hashMap)

    def isPairPresent(self, root, target):
        hashMap = {}
        self.inOrder(root, target, hashMap)
        return self.founded
