# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.
from unittest import result


class Solution(object):

    def productExceptSelf(self, nums):
        product = 1
        updated = False
        has_zero = 0
        for value in nums:
            if value == 0:
                has_zero += 1
                continue
            updated = True
            product *= value
        result = []
        for value in nums:
            if has_zero != 0:
                if value == 0 and updated and has_zero == 1:
                    result.append(product)
                else:
                    result.append(0)
            else:
                result.append(product // value)

        return result


obj = Solution()
print(obj.productExceptSelf([0, 4, 0]))
