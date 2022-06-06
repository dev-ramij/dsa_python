class Solution(object):

    def maxSubArray(self, nums):
        if len(nums) == 0:
            return "None"
        max_sum = nums[0]
        cont_sum = nums[0]
        cont = False
        for i, value in enumerate(nums):
            if i == 0:
                continue
            if cont_sum + value > 0:
                cont = True
                cont_sum += value
            else:
                cont_sum = 0
                cont = False
            if (value >= cont_sum or not cont) and value >= max_sum:
                print("Eter: ",i+1)
                max_sum = value
                cont_sum = value
            elif cont_sum >= max_sum and cont_sum >= value and cont:
                max_sum = cont_sum
            print(i+1,value,cont_sum,cont,max_sum)
        return max_sum


objects = Solution()
print(objects.maxSubArray([-1,0,-2,2]))
