# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.


class Solution(object):

    def search(self, nums, target):
        for i in range(len(nums)):
            curr_idx = len(nums) - 1 - i
            if nums[curr_idx] == target:
                return curr_idx
            if curr_idx == 0:
                return -1
            if nums[curr_idx] < nums[curr_idx - 1]:
                first = curr_idx
                last = len(nums) - 1
                if target > nums[last]:
                    first = 0
                    last = curr_idx -1
                while first <= last:

                    mid = (first + last) // 2
                    if target == nums[mid]:
                        return mid
                    if target < nums[mid]:
                        last = mid - 1
                    else:
                        first = mid + 1
        return -1


objects = Solution()
print(objects.search([4, 5, 6, 7, 0, 1, 2], 6))
