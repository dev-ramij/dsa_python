import heapq


class Solution:

    # sort the array
    # fill the hashmap with desired position
    # for ex. [2,8,5,4] hash = {2:0,8:3,5:2,4:1}
    # compare if it is in right position
    # swap it to its right position
    # check again step 3 for the updated item
    def minSwaps(self, nums):
        count = 0
        n = len(nums)
        hashMap ={}
        sorted_array = nums.copy()
        sorted_array.sort()
        for i in range(n):
            hashMap[sorted_array[i]] = i
        for i in range(n):
            # suppose [1,3,4,2,5] -> [1,2,3,4,5]
            # for 3 position will be 2 so swap
            # current [1,4,3,2,5]
            # still i 1 holds wrong element so swap again
            while hashMap[nums[i]] != i:
                count +=1 
                first_pos = i
                sec_pos = hashMap[nums[i]]
                nums[first_pos],nums[sec_pos] = nums[sec_pos],nums[first_pos]
        return count


a = [2,8,5,3]
a[0],a[2] = a[2],a[0]
print(a)

o = Solution()
print(o.minSwaps([2,8,5,4]))

