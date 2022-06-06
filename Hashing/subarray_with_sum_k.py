class Solution:

    def findSubArraySum(self, arr, n, k):
        count = 0
        sum = 0
        # hashmap is used to store previous sum
        hashMap = {}
        for i in range(n):
            sum += arr[i]
            # if current sum is equal to required number then increase the count
            if sum == k:
                count += 1
            # if currsum -k is present in previous sum then we will increment count
            # There may be multiple previous sum present  
            if (sum - k) in hashMap:
                count += hashMap[sum - k]
            if sum in hashMap:
                hashMap[sum] +=1
            else:
                hashMap[sum] = 1
        return  count

ob = Solution()
print(ob.findSubArraySum([10, 2, -2, -20, 10], 5, -10))
