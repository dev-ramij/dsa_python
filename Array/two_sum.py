class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            if target < nums[i]:
                continue
            diff = target - nums[i]
            print("diff: ",diff)
            for j in range(len(nums)):
                if i == j:
                    continue
                if diff == nums[j]:
                    return [i,j]

obj = Solution()
print(obj.twoSum([-1,-2,-3,-4,-5],-8))