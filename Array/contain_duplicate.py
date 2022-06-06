class Solution(object):

    def containsDuplicate(self, nums):
        seen = {}
        for num in nums:
            if num in seen:
                return "true"
            else:
                seen[num] = True
                print(seen)
        return "false"

obj =Solution()
print(obj.containsDuplicate([1,2,3,4]))
