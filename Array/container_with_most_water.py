# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.


class Solution(object):

    def maxArea(self, height):
        maximumArea = 0
        leftPointer = 0
        rightPointer = len(height) - 1
        while leftPointer <= rightPointer:
            localArea = min(height[leftPointer], height[rightPointer]) * (
                rightPointer - leftPointer)
            if localArea > maximumArea:
                maximumArea = localArea
            if height[leftPointer] <= height[rightPointer]:
                leftPointer = leftPointer + 1
            else:
                rightPointer = rightPointer - 1
        return maximumArea

obj = Solution()
print(obj.maxArea([1,8,6,2,5,4,8,3,7]))
