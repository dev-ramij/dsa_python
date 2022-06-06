

class Solution:
    #Four condition may be possible
    # 1. root is n1 or n2 if so the other value will be its child so lca will be root
    # 2. n1 is present in the left subtree and n2 is present in the right subtree. In that case, root will be the lca
    # 3. n1 and n2 is present in left or right. Then left or right will be the lca
    # 4. n1 and n2 is not present then None will be returned
    def lca(self,root, n1, n2):
        # if root is None then return none
        # it will happened if we couldn't find any of n1 and n2 and goes to the leaf end (cond 4)
        if root is None:
            return None
        # if root is lca (cond 1)
        if root.data == n1 or root.data == n2:
            return root
        # get the lca from left subtree
        left = self.lca(root.left, n1, n2)
        # get the lca from right subtree
        right = self.lca(root.right, n1, n2)
        # if left is None then right may contain n1 and n2 (cond 3)
        if left is None:
            return right
        # if right is None then left may contain n1 and n2 (cond 3)
        if right is None:
            return left
        # if left and right both contains n1 and n2 then root will be lca (cond 2)
        return root

ob = Solution()
# ob.lca(root, n1, n2)