# Here we are using hash map to solve the problem

class Solution:
   def twoSum(self, nums, target) :
       seen = {}
       for i, value in enumerate(nums):
           remaining = target - value
           
           if remaining in seen:
               return [i, seen[remaining]]
            
           seen[value] = i 
           print(seen)

obj = Solution()
print(obj.twoSum([-1,-2,-3,-4,-5],-8))