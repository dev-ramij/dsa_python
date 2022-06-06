# Given an unsorted array arr[] of size N. Rotate the array to the left (counter-clockwise direction) by D steps,
# where D is a positive integer.


class Solution:

    def rotateArr(self, A, D, N):
        left_array = A[:D]
        right_array = A[D:]
        A = left_array + right_array


ob = Solution()
ob.rotateArr([1, 2, 3, 4, 5], 2, 5)
