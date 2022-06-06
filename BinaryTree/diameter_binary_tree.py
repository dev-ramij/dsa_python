class Solution:
    
    maximum = 0

    #Calculating the height
    def height(self, root):
        if root is None:
            return 0
        # left height
        lh = self.height(root.left)
        # right height
        rh = self.height(root.right)
        diameter = lh + rh +1
        # if diameter is greater than maximum then update
        if self.maximum < diameter:
            self.maximum = diameter
        return max(lh, rh) + 1

    def diameter(self, root):
        if root is None:
            return 0
        
        self.height(root)
        return self.maximum
