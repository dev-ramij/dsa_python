# Given an array of size N-1 such that it only contains distinct integers in the range of 1 to N. Find the missing element.

class Solution:
    def MissingNumber(self,array,n):
        return ((n*(n+1))//2) - sum(array)

objects = Solution()
print(objects.MissingNumber([1,2,3,5],5))

