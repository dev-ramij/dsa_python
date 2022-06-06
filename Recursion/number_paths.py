# The problem is to count all the possible paths
# from top left to bottom right of a MxN matrix with the constraints
# that from each cell you can either move to right or down.


class Solution:

    def numberOfPaths(self, n, m):

        if n == 1:
            return 1
        if m == 1:
            return 1
        return self.numberOfPaths(n - 1, m ) + self.numberOfPaths(n, m - 1)


objects = Solution()
print(objects.numberOfPaths(2,8))
