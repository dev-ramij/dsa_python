# Given an unsorted array arr[] of n positive integers.
# Find the number of triangles that can be formed with three different array elements
# as lengths of three sides of triangles.


class Solution:

    def findNumberOfTriangles(self, arr, n):
        if n < 3:
            return 0
        if n == 3:
            return 1
        count = 0
        arr.sort()
        for i in range(n - 2):
            l = 0
            curr_idx = n - 1 - i
            r = curr_idx - 1

            while l < r:
                if arr[l] + arr[r] > arr[curr_idx]:
                    count += (r - l)
                    r -= 1
                else:
                    l += 1
        return count


objects = Solution()
print(objects.findNumberOfTriangles([4, 4, 6, 7, 8, 9], 6))
