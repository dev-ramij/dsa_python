## If the sum is negative then discard the part and go on


class Solution(object):

    def maxSubArray(self, nums):
        max_sum = -1000000000000000  ## for all negative number
        curr_sum = 0
        for i, value in enumerate(nums):
            curr_sum += value
            if curr_sum > max_sum:
                max_sum = curr_sum

            if curr_sum < 0:
                curr_sum = 0

        return max_sum


obj = Solution()
obj.maxSubArray([-2, -1])
