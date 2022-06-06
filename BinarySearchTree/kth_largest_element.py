class Solution:
    # inorder travrsal gives sorted array of BST
    def inOrder(self, root, res_arr):
        self.inOrder(root.left, res_arr)
        res_arr.append(root.data)
        self.inOrder(root.right, res_arr)

    def kthLargest(self, root, k):
        res_arr = []
        self.inOrder(root, res_arr)
        # reversed for finding largest
        res_arr.sort(reverse=True)
        return res_arr[k-1]