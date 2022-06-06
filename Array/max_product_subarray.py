## If the sum is negative then discard the part and go on


class Solution(object):

    def maxProduct(self, nums):
        maxP, minP, result = nums[0], nums[0], nums[0]
        for i, value in enumerate(nums):
            if i == 0:
                continue
            x = max(value, maxP * value, minP * value)
            y = min(value, maxP * value, minP * value)
            maxP, minP = x, y
            result = max(result, maxP)
        return result


obj = Solution()
print(obj.maxProduct([-2, 0, -1]))
