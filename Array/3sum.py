# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.


class Solution(object):

    def threeSum(self, nums):
        result = []
        if len(nums) < 3:
            return result
        nums.sort()
        for i in range(len(nums)-2):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j]) > 0:
                    break
                rem = 0 - (nums[j] + nums[i])
                if rem in nums[j + 1:]:
                    arr = [nums[i], nums[j], rem]
                    if arr not in result:
                        result.append(arr)

        return result


obj = Solution()
print(obj.threeSum([-2, 0, 1, 1, 2]))
